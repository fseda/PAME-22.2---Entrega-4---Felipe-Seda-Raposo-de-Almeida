from app.extensions import ma
# from app.purchase import PurchaseSchema


class UserSchema(ma.Schema):
    id = ma.Integer(dump_only=True)

    # Define se o usuário é administrador ou cliente
    is_admin = ma.Boolean(required=True)
    
    username = ma.String(required=True)
    password = ma.String(required=True)

    email = ma.String(required=True)
    name = ma.String(required=True)
    age = ma.Int(required=True)
    cpf = ma.String(required=True)

    address = ma.String(required=True)

    # purchases = ma.Nested('PurchaseSchema')



