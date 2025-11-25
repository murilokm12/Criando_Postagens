# 📝 TechBlog – Projeto CRUD com Flask + SQLite

Este projeto é um **desafio educacional** onde os alunos devem criar um pequeno **sistema de blog** utilizando:

- **Flask**
- **SQLite3**
- **HTML + CSS**
- Estrutura básica com `templates/` e `static/`

O objetivo é aprender CRUD completo: **Criar, Ler, Editar e Deletar** publicações.

---

## 📌 Objetivo do Projeto

Criar uma plataforma simples de blog onde:

- A **Home** exibe as publicações para os usuários.
- A **Área Admin** permite ao proprietário:
  - Criar novas postagens  
  - Editar postagens  
  - Excluir postagens  

Tudo isso utilizando uma interface simples, estilizada e funcional.

---

## 📁 Estrutura do Projeto

```
meu_blog/
│
├── app.py
│
├── static/
│   └── css/
│       └── style.css
│
└── templates/
    ├── index.html
    ├── admin.html
    ├── editar.html
    └── novo_post.html
```

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Flask**
- **SQLite3**
- **HTML5**
- **CSS3**

---

## ▶️ Como Executar

1. Instale o Flask (se ainda não instalou):

```bash
pip install flask
```

2. Execute o projeto:

```bash
python app.py
```

3. Acesse no navegador:

```
http://127.0.0.1:5000/
```

---

## 📚 Funcionalidades do CRUD

### ✔ Criar post  
Formulario → Salva no banco → Exibe no admin

### ✔ Ler posts  
Home exibe todos  
Admin exibe todos com botões

### ✔ Editar post  
Carrega os dados → Formulário → Atualiza no banco

### ✔ Deletar post  
Admin → Botão de excluir → Remove do banco

---

## 🎨 Layout

O estilo do site segue o design moderno fornecido como referência:  
- Cabeçalho estilizado  
- Cards organizados  
- Tipografia elegante  
- Layout limpo e responsivo  

(CSS incluso no projeto)

---

## 🎯 Aprendizados do Aluno

Ao finalizar o desafio, o aluno terá aprendido:

- Construir rotas Flask
- Conectar ao SQLite
- Criar tabelas com SQL
- Manipular dados com CRUD
- Usar `request.form`
- Renderizar páginas com Jinja (`render_template`)
- Organizar projeto com `templates/` e `static/`

---

## 👨‍🏫 Autor

Atividade criada para fins educacionais  
Professor: **Seu nome aqui**  
Com apoio do ChatGPT 🤖

---

Se quiser, posso gerar uma **versão com badges**, **versão com imagem de preview**, ou **README profissional estilo GitHub Pro**.  

Só pedir.
