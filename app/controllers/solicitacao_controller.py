from flask import render_template, request
from datetime import datetime

class SolicitacaoController:
    def criar(self):
        return render_template('solicitacao/criar.html')
    
    def acompanhar(self):
        # Simulando banco de dados
        solicitacoes_db = [
            { 
                "id": 1, "rua": "Avenida dos Pioneiros", "numero": "45", "bairro": "Centro", 
                "descricao": "Boca de Lobo entortada e com rachaduras", "categoria": "Manutenção de Boca de Lobo", 
                "status": "Em Análise", "data_agendamento": None, "data_finalizacao": None, "gravidade": "Baixa"
            },
            { 
                "id": 2, "rua": "Travessa dos Girassóis", "numero": "789", "bairro": "Vila Nova", 
                "descricao": "Boca de Lobo aberta próxima à escola municipal", "categoria": "Reposição de Boca de Lobo", 
                "status": "Concluída", "data_agendamento": "2025-10-20", "data_finalizacao": "2025-10-25", "gravidade": "Alta"
            }
        ]
        
        # Converte datas de string para datetime
        for s in solicitacoes_db:
            for campo in ["data_agendamento", "data_finalizacao"]:
                if s[campo] and isinstance(s[campo], str):
                    try:
                        s[campo] = datetime.strptime(s[campo], "%Y-%m-%d")
                    except ValueError:
                        s[campo] = None

        status_filtro = request.args.get('status', '')
        if status_filtro:
            dados_filtrados = [s for s in solicitacoes_db if s['status'] == status_filtro]
        else:
            dados_filtrados = solicitacoes_db

        return render_template(
            'solicitacao/acompanhar.html',
            solicitacoes=dados_filtrados,
            filtro_ativo=status_filtro
        )
