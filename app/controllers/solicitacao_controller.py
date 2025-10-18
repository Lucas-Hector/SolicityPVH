from flask import render_template, request
from datetime import datetime


class SolicitacaoController:
    def criar(self):
        return render_template('solicitacao/criar.html')
    
    def minhas_solicitacoes(self):
        solicitacoes_db = [
            { 
                "id": 1, "endereco": "Rua das Acácias, 123", "descricao": "Vários buracos perigosos na via.", 
                "categoria": "Tapa-buracos", "status": "Pendente", "justificativa": "", "data_agendamento": None
            },
            { 
                "id": 2, "endereco": "Avenida dos Pioneiros, 456", "descricao": "Poste de sinalização de 'PARE' caído.", 
                "categoria": "Sinalização viária", "status": "Em Análise", "justificativa": "", "data_agendamento": None 
            },
            { 
                "id": 3, "endereco": "Travessa dos Girassóis, 789", "descricao": "Tampa de bueiro quebrou, criando um buraco.", 
                "categoria": "Reparo em bueiro", "status": "Agendada", "justificativa": "Equipe C irá ao local.", "data_agendamento": "2025-10-20"
            },
            { 
                "id": 4, "endereco": "Rua Principal, em frente ao nº 1000", "descricao": "Asfalto completamente desgastado.", 
                "categoria": "Recapeamento", "status": "Concluída", "justificativa": "Obra finalizada pela equipe B em 15/10.", "data_agendamento": "2025-10-14" 
            }
        ]
        
        for s in solicitacoes_db:
            if s["data_agendamento"] is not None:
                s["data_agendamento"] = datetime.strptime(s["data_agendamento"], "%Y-%m-%d")

        status_filtro = request.args.get('status', '')

        if status_filtro:
            dados_filtrados = [s for s in solicitacoes_db if s['status'] == status_filtro]
        else:
            dados_filtrados = solicitacoes_db

        return render_template(
            'solicitacao/minhas_solicitacoes.html',
            solicitacoes=dados_filtrados,
            filtro_ativo=status_filtro
        )
        