from app.extensions import ma

class SizeSchema(ma.Schema):
    id = ma.Integer(dump_only=True)
    size = ma.String(required=True)
    quantity = ma.Integer(required=True)

class ItemSchema(ma.Schema):
    id = ma.Integer(dump_only=True)

    title = ma.String(required=True)
    type_of_product = ma.String(required=True)
    price = ma.Float(required=True)
    description = ma.String(required=True)
    sizes = ma.List(ma.Nested(SizeSchema, required=True))