from app.extensions import ma

class SaleSchema(ma.Schema):
    id = ma.Integer(dump_only=True)
    
    user_id = ma.Integer(required=True)
    item_id = ma.Integer(required=True)
    item_size_id = ma.Integer(required=True)
    quantity = ma.String(required=True)
    total_price = ma.Float(dump_only=True)