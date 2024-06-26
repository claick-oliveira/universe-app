from flask import request

from ..app import app
from ..controllers.planets import (
  list_all_planets_controller,
  get_planet_controller,
  create_planet_controller,
  update_planet_controller,
  delete_planet_controller
)


@app.route("/planets", methods=['GET', 'POST'])
def list_create_planets():
    if request.method == 'GET':
        return list_all_planets_controller()
    if request.method == 'POST':
        return create_planet_controller()
    else:
        return 'Method is Not Allowed'


@app.route("/planets/<id>", methods=['GET', 'PUT', 'DELETE'])
def retrieve_update_destroy_planets(id):
    if request.method == 'GET':
        return get_planet_controller(id)
    if request.method == 'PUT':
        return update_planet_controller(id)
    if request.method == 'DELETE':
        return delete_planet_controller(id)
    else:
        return 'Method is Not Allowed'
