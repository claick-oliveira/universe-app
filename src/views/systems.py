from flask import request

from ..app import app
from ..controllers.systems import (
  list_all_systems_controller,
  get_system_controller,
  create_system_controller,
  update_system_controller,
  delete_system_controller
)

from ..controllers.stars import (
  list_all_stars_system_controller,
  create_star_controller
)

from ..controllers.planets import (
  list_all_planets_system_controller,
  create_planet_controller
)


@app.route("/systems", methods=['GET', 'POST'])
def list_create_systems():
    if request.method == 'GET':
        return list_all_systems_controller()
    if request.method == 'POST':
        return create_system_controller()
    else:
        return 'Method is Not Allowed'


@app.route("/systems/<id>", methods=['GET', 'PUT', 'DELETE'])
def retrieve_update_destroy_systems(id):
    if request.method == 'GET':
        return get_system_controller(id)
    if request.method == 'PUT':
        return update_system_controller(id)
    if request.method == 'DELETE':
        return delete_system_controller(id)
    else:
        return 'Method is Not Allowed'


@app.route("/systems/<id>/stars", methods=['GET', 'POST'])
def list_create_stars_system(id):
    if request.method == 'GET':
        return list_all_stars_system_controller(id)
    if request.method == 'POST':
        return create_star_controller(id)
    else:
        return 'Method is Not Allowed'


@app.route("/systems/<id>/planets", methods=['GET', 'POST'])
def list_create_planets_system(id):
    if request.method == 'GET':
        return list_all_planets_system_controller(id)
    if request.method == 'POST':
        return create_planet_controller(id)
    else:
        return 'Method is Not Allowed'
