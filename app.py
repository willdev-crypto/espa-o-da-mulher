from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from forms import LoginForm, ProductForm, RegisterForm
import os

# Inicialização do Flask e SQLAlchemy
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(app.instance_path, "your_database.db")}'
db = SQLAlchemy(app)

# Modelo de Produto
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    barcode = db.Column(db.String(13), nullable=False, unique=True)
    quantity = db.Column(db.Integer, nullable=False)

# Modelo de Usuário
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    rg = db.Column(db.String(20), nullable=True)
    cpf = db.Column(db.String(14), nullable=True)
    phone = db.Column(db.String(11), nullable=True)
    is_admin = db.Column(db.Boolean, default=False)

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para ver todos os produtos
@app.route('/products')
def products():
    all_products = Product.query.all()
    is_admin = True  # Implementar lógica real para verificar se o usuário é admin
    return render_template('products.html', products=all_products, is_admin=is_admin)

# Rota para adicionar um novo produto
@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    form = ProductForm()
    if form.validate_on_submit():
        new_product = Product(
            name=form.name.data,
            price=form.price.data,
            barcode=form.barcode.data,
            quantity=form.quantity.data
        )
        db.session.add(new_product)
        db.session.commit()
        flash('Produto adicionado com sucesso!', 'success')
        return redirect(url_for('products'))
    is_admin = True  # Implementar lógica real para verificar se o usuário é admin
    return render_template('add_product.html', form=form, is_admin=is_admin)

# Rota para o login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            is_admin = user.is_admin
            users = User.query.all()
            return render_template('login.html', form=form, users=users, is_admin=is_admin)
        else:
            flash('Usuário ou senha inválidos', 'danger')
    return render_template('login.html', form=form)

# Rota para cadastro de usuário
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(
            username=form.username.data,
            password=form.password.data,
            rg=form.rg.data,
            cpf=form.cpf.data,
            phone=form.phone.data
        )
        db.session.add(new_user)
        db.session.commit()
        flash('Usuário cadastrado com sucesso!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

# Rota para remover um usuário
@app.route('/remove_user/<int:user_id>', methods=['POST'])
def remove_user(user_id):
    is_admin = True  # Implementar lógica real para verificar se o usuário é admin
    if not is_admin:
        return redirect(url_for('index'))
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        flash('Usuário removido com sucesso!', 'success')
    return redirect(url_for('users'))

# Rota para visualizar todos os usuários
@app.route('/users')
def users():
    is_admin = True  # Implementar lógica real para verificar se o usuário é admin
    if not is_admin:
        return redirect(url_for('index'))
    
    all_users = User.query.all()
    return render_template('users.html', users=all_users, is_admin=is_admin)

# Rota para visualizar o perfil de um usuário específico

@app.route('/user/<int:user_id>')
def user_profile(user_id):
    is_admin = True  # Substitua isso pela lógica real de verificação de admin..
    if not is_admin:
        return redirect(url_for('index'))
    user = User.query.get(user_id)
    if user:
        return render_template('user_profile.html', user=user)
    else:
        flash('Usuário não encontrado', 'danger')
        return redirect(url_for('users'))


# Inicializa a aplicação
if __name__ == '__main__':
    if not os.path.exists(app.instance_path):
        os.makedirs(app.instance_path)
    with app.app_context():
        db.create_all()
    app.run(debug=True)
