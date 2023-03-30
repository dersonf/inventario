###############################################################
# descrição      : Inventário de hosts e updates
# autor          : Anderson Ferneda
# email          : anderson79@bol.com.br
# data           : 03/03/2023
###############################################################

from app import app, db
from app.models import User, Hosts, Updates


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Hosts': Hosts, 'Updates': Updates}

