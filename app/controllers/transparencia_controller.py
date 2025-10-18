from flask import render_template


class TransparenciaController:
    def dashboard(self):
        return render_template('transparencia/dashboard.html')
    
    