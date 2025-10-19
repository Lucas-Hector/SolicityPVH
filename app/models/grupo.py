from . import db

class Grupo(db.Model):
    __tablename__ = 'grupo'

    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.String(100))

    usuarios = db.relationship('Usuario', back_populates='grupo')
