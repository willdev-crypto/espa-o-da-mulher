from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FloatField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError
import re

# Validador personalizado para a senha
def validate_password(form, field):
    password = field.data
    if not re.search(r'\d', password) or not re.search(r'[a-zA-Z]', password) or len(password) < 4:
        raise ValidationError('A senha deve ter pelo menos 4 dígitos numéricos e letras.')

# Formulário de Login
class LoginForm(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired(), Length(min=4, max=25)])
    password = PasswordField('Senha', validators=[DataRequired(), validate_password])
    submit = SubmitField('Entrar')

# Formulário de Cadastro de Produtos
class ProductForm(FlaskForm):
    name = StringField('Nome', validators=[DataRequired()])
    price = FloatField('Preço', validators=[DataRequired(), NumberRange(min=0)])
    barcode = StringField('Código de Barras', validators=[DataRequired()])
    quantity = IntegerField('Quantidade', validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField('Adicionar Produto')

# Formulário de Cadastro de Usuário
class RegisterForm(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired(), Length(min=4, max=25)])
    password = PasswordField('Senha', validators=[DataRequired(), validate_password])
    rg = StringField('RG', validators=[Length(max=20)])
    cpf = StringField('CPF', validators=[Length(max=14)])
    phone = StringField('Telefone', validators=[Length(max=11)])
    submit = SubmitField('Cadastrar')
