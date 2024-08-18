import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'sua_chave_secreta_aqui'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///perfumaria.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# config.py
class Config:
    SECRET_KEY = 'your_secret_key_here'
    # Adicione outras configurações aqui, como configurações de banco de dados
