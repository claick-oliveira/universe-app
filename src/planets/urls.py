from flask import request

from ..app import app
from .controllers import list_all_planets_controller


@app.route("/planets", methods=['GET', 'POST'])
def list_create_planets():
    if request.method == 'GET':
        return list_all_planets_controller()
    # if request.method == 'POST': return create_account_controller()
    else:
        return 'Method is Not Allowed'
