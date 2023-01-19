from app.users.models import users


def get_last_id(arr):
    last = arr[-1]
    return last['id']

def is_admin(user_id):
    for user in users:
            if user['id'] == user_id:
                return user['is_admin']
