from flask import render_template


class AutenticacaoController:
    def index(self):
        return render_template('autenticacao/index.html')