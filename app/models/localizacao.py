from . import db

class Localizacao(db.Model):
    __tablename__ = 'localizacao'

    cep = db.Column(db.String(10), primary_key=True)
    rua = db.Column(db.String(120))
    numero = db.Column(db.String(10))
    bairro = db.Column(db.String(100))
    ponto_referencia = db.Column(db.String(150))

    solicitacoes = db.relationship('Solicitacao', back_populates='localizacao')
