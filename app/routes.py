from mvc_flask import Router

Router.get('/', 'home#index')

Router.get('/autenticacao', 'autenticacao#index')

Router.get('/transparencia', 'transparencia#dashboard')

Router.get('/solicitacao/acompanhar', 'solicitacao#acompanhar')
Router.get('/solicitacao/criar', 'solicitacao#criar')
