from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from forms import LoginForm
import os

# Inicializa a aplicação Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Adicione uma chave secreta
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///perfumaria.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o SQLAlchemy
db = SQLAlchemy(app)

# Define o modelo User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Rota para login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            # Autenticação bem-sucedida
            return redirect(url_for('index'))
        else:
            flash('Usuário ou senha inválidos', 'danger')  # Mensagem de erro
    return render_template('login.html', form=form)

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('dashboard.html')

if __name__ == "__main__":
    db.create_all()  # Cria as tabelas antes de iniciar o servidor
    app.run(debug=True)

    from app import app, db
from models import User

# Usar o contexto da aplicação
with app.app_context():
    # Consultar todos os usuários
    users = User.query.all()

    # Exibir os usuários
    for user in users:
        print(f'ID: {user.id}, Username: {user.username}')