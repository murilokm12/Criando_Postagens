from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# ------------------------
# Inicialização do Banco
# ------------------------
def init_db():
    conn = sqlite3.connect("blog.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            conteudo TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# ------------------------
# Rota Home - Exibe Posts
# ------------------------
@app.route('/')
def index():
    conn = sqlite3.connect("blog.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

# ------------------------
# Rota - Página Admin
# ------------------------
@app.route('/admin')
def admin():
    conn = sqlite3.connect("blog.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()
    conn.close()
    return render_template('admin.html', posts=posts)

# ------------------------
# Criar Post
# ------------------------
@app.route('/criar', methods=['POST'])
def criar():
    # 1 etapa buscar os valores no html
    titulo = request.form['titulo']
    conteudos = request.form['conteudo']

    conn = sqlite3.connect("blog.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO posts (titulo , conteudo) values(?,?) ",(titulo,conteudos))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


    # 2 conectar com o banco e usar o insert poara inserir os valores 

# ------------------------
# Deletar Post
# ------------------------
@app.route('/deletar/<int:post_id>', methods=['POST'])
def deletar(post_id):
    conn = sqlite3.connect("blog.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM posts where id=? ", (post_id))
    posts = cursor.fetchall()
    conn.close()
    return render_template('index.html', posts=posts)
   

# ------------------------
# Página de Edição
# ------------------------
@app.route('/editar/<int:post_id>')
def editar(post_id):
    conn = sqlite3.connect("blog.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts WHERE id = ?", (post_id,))
    post = cursor.fetchone()
    conn.close()
    return render_template("editar.html", post=post)

# ------------------------
# Salvar Edição
# ------------------------
@app.route('/editar/<int:post_id>', methods=['POST'])
def salvar_edicao(post_id):
    titulo = request.form['titulo']
    conteudo = request.form['conteudo']

    conn = sqlite3.connect("blog.db")
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE posts SET titulo = ?, conteudo = ? WHERE id = ?
    """, (titulo, conteudo, post_id))
    conn.commit()
    conn.close()

    return redirect(url_for('admin'))

app.run(debug=True)
