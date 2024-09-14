class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    rg = db.Column(db.String(20), nullable=True)
    cpf = db.Column(db.String(14), nullable=True)
    phone = db.Column(db.String(11), nullable=True)
