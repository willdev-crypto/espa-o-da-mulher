from flask import Flask, render_template, request, redirect, url_for
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Adicione uma chave secreta

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Adicione lógica de autenticação aqui
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

@app.route('/')
def index():
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.run(debug=True)
