from flask import request
from flask.views import MethodView

from .models import items
from .schema import ItemSchema
from app.helpers import get_last_id, is_admin

class ItemController(MethodView):

    # Criar Item
    def post(self, user_id = -1):
        # Apenas autorizar se usuario for administrador
        if not is_admin(user_id):
            return {}, 401 # 401 - Unauthorized

        schema = ItemSchema()
        data = request.json
        data['id'] = get_last_id(items) + 1

        try:
            item = schema.dump(data)
            items.append(item)
        except:
            print('Error')
            return {}, 400 # 400 - Bad Request

        return item, 201 # 201 - OK

    def get(self, user_id = -1):
        schema = ItemSchema()
        return schema.dump(items, many=True), 200 # 200 - OK
    
class ItemDetails(MethodView):
    # Retornar item por id
    def get(self, item_id, user_id = -1):
        schema = ItemSchema()
                
        for item in items:
            if item['id'] == item_id:
                return schema.dump(item), 200 # 200 - OK
        
        return {}, 400

    # Atualizar algum dado do usuario
    def put(self, item_id, user_id = -1):
        if not is_admin(user_id):
            return {}, 401

        schema = ItemSchema()
        data = request.json

        item_index = -1

        for item in items:
            if item['id'] == item_id:
                item_index = items.index(item)
        
        if item_index == -1:
            return {}, 400 # 400 - Not found
        
        data['id'] = item_id
        new_item = schema.dump(data)
        items[item_index] = new_item

        return new_item, 201

    def patch(self, item_id, user_id = -1):
        if not is_admin(user_id):
            return {}, 401
        
        schema = ItemSchema()
        data = request.json

        item_index = -1

        for item in items:
            if item['id'] == item_id:
                item_index = items.index(item)
        
        if item_index == -1:
            return {}, 400 # 400 - Not found

        item = items[item_index]

        title = data.get('title', item['title'])
        type_of_product = data.get('type_of_product', item['type_of_product'])
        price = data.get('price', item['price'])
        description = data.get('description', item['description'])
        sizes = data.get('sizes', item['sizes'])

        data['title'] = title
        data['type_of_product'] = type_of_product
        data['price'] = price
        data['description'] = description
        data['sizes'] = sizes

        item = schema.dump(data)
        items[item_index] = item

        return item, 201
    
    def delete(self, item_id, user_id = -1):
        if not is_admin(user_id):
            return {}, 401
        
        for item in items:
            if item['id'] == item_id:
                items.remove(item)
                return {}, 204 # No Content
        
        return {}, 404 # Not Found