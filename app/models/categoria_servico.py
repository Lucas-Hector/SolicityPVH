from . import db

class CategoriaServico(db.Model):
    __tablename__ = 'categoria_servico'

    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(100), nullable=False)

    solicitacoes = db.relationship('Solicitacao', back_populates='categoria')
