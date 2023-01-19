from flask import request
from flask.views import MethodView

from .models import users
from .schema import UserSchema
from app.helpers import get_last_id

class UserController(MethodView):

    # Criar um usuario
    def post(self):
        schema = UserSchema()
        data = request.json
        data['id'] = get_last_id() + 1

        # data['birthday'] = datetime.date.isoformat(data['birthday'])

        # Verificar se ja existe um usuario com aquele username e email
        for user in users:
            if data['username'] == user['username']:
                return {
                    "msg": "Esse usuśrio já existe."
                }, 400
            if data['email'] == user['email']:
                return {
                    "msg": "Esse email já está cadastrado."
                }, 400
        
        try:
            user = schema.dump(data)
            users.append(user)
        except:
            print('Error')
            return {}, 400 # 400 - Bad Request
        
        return user, 201 # 201 - Created

    # Retornar todos os usuarios
    def get(self):
        schema = UserSchema()
        return schema.dump(users, many=True), 200 # 200 - OK
    
class UserDetails(MethodView):
    # Retornar usuario por id
    def get(self, id):
        schema = UserSchema()
                
        for user in users:
            if user['id'] == id:
                return schema.dump(user), 200 # 200 - OK
        
        return {}, 400
    
    # Atualizar algum dado do usuario
    def put(self, id):
        schema = UserSchema()
        data = request.json

        user_index = -1

        for user in users:
            if user['id'] == id:
                user_index = users.index(user)
        
        if user_index == -1:
            return {}, 400 # 400 - Not found
        
        data['id'] = id
        new_user = schema.dump(data)
        users[user_index] = new_user

        return new_user, 201

    def patch(self, id):
        schema = UserSchema()
        data = request.json

        user_index = -1

        for user in users:
            if user['id'] == id:
                user_index = users.index(user)
        
        if user_index == -1:
            return {}, 400 # 400 - Not found

        user = users[user_index]

        is_admin = data.get('is_admin', user['is_admin'])
        username = data.get('username', user['username'])
        password = data.get('password', user['password'])
        email = data.get('email', user['email'])
        name = data.get('name', user['name'])
        age = data.get('age', user['age'])
        cpf = data.get('cpf', user['cpf'])
        address = data.get('address', user['address'])

        data['is_admin'] = is_admin
        data['username'] = username
        data['password'] = password
        data['email'] = email
        data['name'] = name
        data['age'] = age
        data['cpf'] = cpf
        data['address'] = address

        user = schema.dump(data)
        users[user_index] = user

        return user, 201
        
    def delete(self, id):
        for user in users:
            if user['id'] == id:
                users.remove(user)
                return {}, 204 # No Content
       
        return {}, 404 # Not Found

