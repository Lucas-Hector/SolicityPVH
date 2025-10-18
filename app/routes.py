from mvc_flask import Router

Router.get('/', 'home#index')

Router.get('/autenticacao', 'autenticacao#index')

Router.get('/transparencia', 'transparencia#dashboard')

Router.get('/solicitacao/criar', 'solicitacao#criar')
Router.get('/solicitacao/minhas', 'solicitacao#minhas_solicitacoes')