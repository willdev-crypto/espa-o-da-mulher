

# Adm

Bem-vindo ao projeto **Administração Home**, a solução ideal para gerenciar a perfumaria **O Espaço da Mulher**. Este aplicativo foi desenvolvido para facilitar o controle de estoque, gestão de vendas e muito mais, com uma interface web simples e intuitiva.

## Funcionalidades

- **Controle de Estoque:** Gerencie e atualize o estoque de produtos com facilidade.
- **Adição de Produtos:** Adicione novos produtos ao estoque rapidamente, incluindo informações como nome, preço original, código de barras, quantidade e preço de venda.
- **Gestão de Vendas:** Acompanhe o que entra e sai do estoque com um controle de vendas detalhado.
- **Tela de Venda com Scanner:** Use a tela de vendas para escanear produtos e atualizar o estoque automaticamente.
- **Sistema de Login:** Autentique-se como Administrador (ADM) com acesso total ou como Vendedor com acesso restrito apenas às vendas.
- **Upload de Foto de Perfil:** Todos os usuários podem fazer upload de uma foto de perfil.
- **Importação e Exportação de Relatórios:** Importe e exporte arquivos Excel para relatórios anuais, mensais e diários.
- **Pesquisa e Atualização de Produtos:** Pesquise produtos no estoque e atualize as informações conforme necessário.
- **Cálculo do Volume de Vendas:** Solicite relatórios sobre o volume de vendas para uma visão detalhada do desempenho.

## Requisitos

- **Python 3.11** ou superior
- **Flask** para a criação da aplicação web
- **Flask-WTF** para formulários web
- **OpenPyXL** para manipulação de arquivos Excel

## Instalação

1. **Clone o Repositório:**

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Crie e Ative um Ambiente Virtual:**

   - **No Windows:**

     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

   - **No macOS/Linux:**

     ```bash
     python -m venv venv
     source venv/bin/activate
     ```

3. **Instale as Dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure a Chave Secreta:**

   Edite o arquivo `app.py` e defina a chave secreta para sessões Flask:

   ```python
   app.config['SECRET_KEY'] = 'sua_chave_secreta'
   ```

5. **Execute a Aplicação:**

   ```bash
   python app.py
   ```

   A aplicação estará disponível em [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Estrutura do Projeto

- **app.py:** Arquivo principal da aplicação Flask.
- **templates/:** Diretório contendo os arquivos HTML para renderização das páginas.
- **static/:** Diretório para arquivos estáticos como CSS, JavaScript e imagens.
- **models.py:** Define o modelo de dados para o aplicativo.
- **forms.py:** Define os formulários utilizados na aplicação.
- **config.py:** Configurações do projeto.

## Contribuições

Sinta-se à vontade para contribuir com melhorias, correções de bugs ou novas funcionalidades. Faça um fork do repositório, crie uma branch para suas alterações e envie um pull request.



