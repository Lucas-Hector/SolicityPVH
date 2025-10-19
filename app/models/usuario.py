from . import db

class Usuario(db.Model):
    __tablename__ = 'usuario'

    cpf = db.Column(db.String(14), primary_key=True)
    nome_completo = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(120), unique=True, nullable=False)
    grupo_id = db.Column(db.Integer, db.ForeignKey('grupo.id'), nullable=False)

    grupo = db.relationship('Grupo', back_populates='usuarios')
    solicitacoes = db.relationship('Solicitacao', foreign_keys='Solicitacao.solicitante_id', back_populates='solicitante')
    administradas = db.relationship('Solicitacao', foreign_keys='Solicitacao.administrador_id', back_populates='administrador')
