from flask import Blueprint

from .controller import ItemController, ItemDetails

item_api = Blueprint('item_api', __name__)

# Para administradores
item_api.add_url_rule(
    '/users/<int:user_id>/items/',
    view_func=ItemController.as_view('item_controller_admin_post'),
    methods=['GET', 'POST']
)
item_api.add_url_rule(
    '/users/<int:user_id>/items/<int:item_id>/',
    view_func=ItemDetails.as_view('item_controller_admin_edit'),
    methods=['GET', 'PUT', 'PATCH', 'DELETE']
)

# Para clientes
item_api.add_url_rule(
    '/items/',
    view_func=ItemController.as_view('item_controller'),
    methods=['GET', 'POST']
)

item_api.add_url_rule(
    '/items/<int:item_id>/',
    view_func=ItemDetails.as_view('item_details'),
    methods=['GET', 'PUT', 'PATCH', 'DELETE']
)

