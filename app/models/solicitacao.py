from . import db

class Solicitacao(db.Model):
    __tablename__ = 'solicitacao'

    id = db.Column(db.Integer, primary_key=True)
    id_categoria = db.Column(db.Integer, db.ForeignKey('categoria_servico.id'), nullable=False)
    descricao = db.Column(db.Text)
    solicitante_id = db.Column(db.String(14), db.ForeignKey('usuario.cpf'), nullable=False)
    foto_antes = db.Column(db.String(255))     # caminho da imagem antes
    foto_depois = db.Column(db.String(255))    # caminho da imagem depois
    localizacao_cep = db.Column(db.String(10), db.ForeignKey('localizacao.cep'), nullable=False)
    status = db.Column(db.String(50))
    data_solicitacao = db.Column(db.DateTime)
    administrador_id = db.Column(db.String(14), db.ForeignKey('usuario.cpf'))
    grau_prioridade = db.Column(db.Integer)
    data_analise = db.Column(db.DateTime)
    data_agendamento = db.Column(db.DateTime)
    data_conclusao = db.Column(db.DateTime)
    feedback = db.Column(db.Text)

    categoria = db.relationship('CategoriaServico', back_populates='solicitacoes')
    solicitante = db.relationship('Usuario', foreign_keys=[solicitante_id], back_populates='solicitacoes')
    administrador = db.relationship('Usuario', foreign_keys=[administrador_id], back_populates='administradas')
    localizacao = db.relationship('Localizacao', back_populates='solicitacoes')
