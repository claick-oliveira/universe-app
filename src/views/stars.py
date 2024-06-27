from flask import request

from ..app import app
from ..controllers.stars import (
  list_all_stars_controller,
  get_star_controller,
  update_star_controller,
  delete_star_controller
)


@app.route("/stars", methods=['GET', 'POST'])
def list_create_stars():
    if request.method == 'GET':
        return list_all_stars_controller()
    else:
        return 'Method is Not Allowed'


@app.route("/stars/<id>", methods=['GET', 'PUT', 'DELETE'])
def retrieve_update_destroy_stars(id):
    if request.method == 'GET':
        return get_star_controller(id)
    if request.method == 'PUT':
        return update_star_controller(id)
    if request.method == 'DELETE':
        return delete_star_controller(id)
    else:
        return 'Method is Not Allowed'
