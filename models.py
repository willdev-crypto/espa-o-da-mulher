class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    rg = db.Column(db.String(20))  # Certifique-se de que a coluna rg está aqui
    cpf = db.Column(db.String(20), unique=True)
    phone = db.Column(db.String(20))
    is_admin = db.Column(db.Boolean, default=False)
