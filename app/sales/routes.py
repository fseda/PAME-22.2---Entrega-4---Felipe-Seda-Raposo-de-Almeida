from flask import Blueprint

from .controller import SaleController, SaleDetails

sale_api = Blueprint('sale_api', __name__)

sale_api.add_url_rule(
    '/users/<int:user_id>/sales/',
    view_func=SaleController.as_view('sale_controller'),
    methods=['GET', 'POST']
)

sale_api.add_url_rule(
    '/users/<int:user_id>/sales/<int:sale_id>/',
    view_func=SaleDetails.as_view('sale_details'),
    methods=['GET']
)