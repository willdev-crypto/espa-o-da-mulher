import os
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Configuração do caminho absoluto para o banco de dados
db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'instance', 'perfumaria.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

# Inicializando o banco de dados e o gerenciador de login
db = SQLAlchemy(app)
login_manager = LoginManager(app)

# Carregar usuário
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Modelo de Usuário
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    rg = db.Column(db.String(20), nullable=False)
    cpf = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

# Modelo de Produto
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    barcode = db.Column(db.String(20), nullable=False, unique=True)
    quantity = db.Column(db.Integer, nullable=False)

# Página de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash('Login bem-sucedido!', 'success')
            return redirect(url_for('index'))
        flash('Credenciais inválidas', 'danger')
    
    users = User.query.all()
    is_admin = current_user.is_authenticated and current_user.is_admin
    return render_template('login.html', users=users, is_admin=is_admin)

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para remover usuário
@app.route('/remove_user/<int:user_id>', methods=['POST'])
@login_required
def remove_user(user_id):
    if not current_user.is_admin:
        flash('Você não tem permissão para remover usuários.', 'danger')
        return redirect(url_for('login'))
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('Usuário removido com sucesso.', 'success')
    return redirect(url_for('login'))

# Rota para visualizar produtos
@app.route('/products')
def products():
    products = Product.query.all()
    is_admin = current_user.is_authenticated and current_user.is_admin
    return render_template('products.html', products=products, is_admin=is_admin)

# Rota para adicionar produto
@app.route('/add_product', methods=['GET', 'POST'])
@login_required
def add_product():
    if not current_user.is_admin:
        flash('Você não tem permissão para adicionar produtos.', 'danger')
        return redirect(url_for('products'))

    if request.method == 'POST':
        name = request.form['name']
        price = float(request.form['price'])
        barcode = request.form['barcode']
        quantity = int(request.form['quantity'])

        # Cria um novo produto e salva no banco de dados
        new_product = Product(name=name, price=price, barcode=barcode, quantity=quantity)
        db.session.add(new_product)
        db.session.commit()

        flash('Produto adicionado com sucesso!', 'success')
        return redirect(url_for('products'))

    return render_template('add_product.html')

# Rota para perfil de usuário
@app.route('/user_profile/<int:user_id>')
@login_required
def user_profile(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('user_profile.html', user=user)

# Inicializa o banco de dados quando o app é executado
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados, se ainda não existirem
        print("Banco de dados inicializado com sucesso!")
    app.run(debug=True)
