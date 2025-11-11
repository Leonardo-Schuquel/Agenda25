# 📒 Agenda Django

Um projeto de **Agenda de Contatos** desenvolvido com **Python e Django**, criado como parte de um curso de aprendizado.  
O sistema permite **gerenciar contatos** de forma segura e organizada, com controle de acesso baseado em autenticação de usuários.

---

## 🚀 Funcionalidades

- 👤 **Sistema de autenticação completo**
  - Registro de novos usuários com verificação de unicidade (`username` e `email` não podem se repetir)
  - Regras de validação de senha para evitar senhas fracas
  - Login, logout e área de perfil de usuário

- 📇 **Gerenciamento de contatos**
  - Criação, edição e exclusão de contatos
  - Apenas o **criador do contato** pode editá-lo ou removê-lo
  - Exibição de detalhes individuais dos contatos

- 🧩 **Controle de acesso dinâmico**
  - Páginas e botões adaptam-se conforme o estado de login do usuário
  - Usuários não autenticados visualizam apenas a lista pública de contatos e opções de login/registro
  - Usuários autenticados veem opções adicionais como **criar contato**, **perfil** e **logout**

- 🖼️ **Interface limpa e responsiva**
  - Layout intuitivo, com tabelas de listagem de contatos e feedback visual (ex: mensagens de sucesso ao logar)

---

## ⚙️ Tecnologias Utilizadas

- **Python 3**
- **Django 5**
- **HTML5 / CSS3**
- **Bootstrap**
- **SQLite3**

---

## 🧠 Conceitos Aplicados

- Autenticação e autorização de usuários (`django.contrib.auth`)
- Criação e manipulação de formulários personalizados (`forms.ModelForm`)
- Restrições de acesso com *decorators* (`@login_required`)
- Mensagens de feedback ao usuário (`django.contrib.messages`)
- Relacionamento entre modelos (`User` ↔ `Contact`)
- Boas práticas de segurança (validação, CSRF, senhas fortes)

---

## 💻 Como Executar o Projeto Localmente

1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
   ```

2. **Crie um ambiente virtual e ative-o**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Aplique as migrações**
   ```bash
   python manage.py migrate
   ```

5. **Crie um superusuário (opcional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Execute o servidor**
   ```bash
   python manage.py runserver
   ```

7. **Acesse o projeto**
   ```
   http://127.0.0.1:8000
   ```

---

## 🔒 Regras de Segurança

- Usuários **não podem ter e-mails ou usernames duplicados**
- As **senhas passam por validações** de complexidade (tamanho mínimo, combinação de caracteres, etc.)
- **Somente o dono do contato** pode editá-lo ou excluí-lo
- **Usuários não logados** têm acesso apenas à visualização pública

---

## 📸 Exemplos de Telas

- Página inicial (não logado)
- Tela de login
- Contatos (usuário autenticado)
- Página de detalhes do contato

*(imagens incluídas no repositório, caso deseje adicionar ao README)*

---

## 🧾 Licença

Este projeto é de uso livre para fins educacionais e pode ser modificado conforme necessário.

---

## ✉️ Autor

**Leonardo Schuquel**  
Desenvolvedor e estudante de Engenharia de Software  
📧 [lschuquel.engsoft@gmail.com](mailto:lchuquel.engsoft@gmail.com)
