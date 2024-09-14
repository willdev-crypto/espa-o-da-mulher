from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user # type: ignore

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    rg = db.Column(db.String(20), nullable=False)
    cpf = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            flash('Login bem-sucedido!', 'success')
            return redirect(url_for('login'))
        flash('Credenciais inválidas', 'danger')
    users = User.query.all()
    is_admin = current_user.is_authenticated and current_user.is_admin
    return render_template('login.html', users=users, is_admin=is_admin)

@app.route('/user_profile/<int:user_id>')
@login_required
def user_profile(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('user_profile.html', user=user)

@app.route('/')
def index():
    return render_template('index.html')


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

@app.route('/register')
def register():
    return 'Página de registro'

@app.route('/')
def index():
    return 'Página inicial'

if __name__ == '__main__':
    app.run(debug=True)

    
