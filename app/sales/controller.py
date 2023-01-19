from flask import request
from flask.views import MethodView

from .models import sales
from app.items.models import items
from .schema import SaleSchema

from app.helpers import get_last_id, is_admin

class SaleController(MethodView):

    def post(self, user_id = -1):
        
        # Admin nao pode comprar 
        if is_admin(user_id):
            return {
                "msg": "Apenas clientes podem comprar"
            }, 401
        
        schema = SaleSchema()
        data = request.json
        data['id'] = get_last_id(sales) + 1

        # Apenas o Usuario pode fazer compras para ele mesmo
        if data['user_id'] is not user_id:
            return {
                "msg": "Voce nao pode comprar para outra pessoa."
            }, 401

        # Apenas autorizar a compra se estiver estoque
        for item in items:
            if data['item_id'] == item['id']:
                price = item['price']

                for sizes in item['sizes']:
                    if data['item_size_id'] == sizes['id']:
                        if data['quantity'] > sizes['quantity']:
                            return {
                                "msg": f"Item sem estoque para o seu pedido, há apenas {sizes['quantity']} em estoque."
                            }, 401
                        else:
                            # Subtrair quantidade da compra do estoque
                            sizes['quantity'] -= data['quantity']

        data['total_price'] = data['quantity'] * price

        sale = schema.dump(data)
        sales.append(sale)

        return sale, 201

    # Buscar todas as compras de um cliente
    def get(self, user_id = -1):
        schema = SaleSchema()

        sales_by_user_id = []
        for  sale in sales:
            if user_id == sale['user_id']:
                sales_by_user_id.append(sale)
            
        if len(sales_by_user_id) == 0:
            return {
                "msg": "Não há pedidos para esse usuario."
            }, 200

        return schema.dump(sales_by_user_id, many=True), 200

class SaleDetails(MethodView):

    def get(self, user_id = -1, sale_id = -1):
        schema = SaleSchema()

        for sale in sales:
            if sale['id'] == sale_id:
                if sale['user_id'] != user_id:
                    return {
                        "msg": "Voce nao pode acessar essa compra."
                    }, 403
                else:
                    return schema.dump(sale), 200

        return {}, 400
        
        