from mvc_flask import Router

Router.get('/', 'home#index')

Router.get('/autenticacao', 'autenticacao#index')

Router.get('/transparencia', 'transparencia#dashboard')

# Router.all('solicitacao', only='criar')