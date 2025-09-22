
from flask import current_app, request

from app.models.user import Users, db


def register():
    data = request.get_json()  # 从请求体里解析 JSON
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return {'code': 400, 'msg': 'username or password missing'}

    user = Users(username=username)
    user.set_password(password)  # 加密密码

    with current_app.app_context():
        db.session.add(user)
        db.session.commit()

    return {'code': 200, 'msg': 'success'}

def login():
    data = request.get_json()  # 从请求体里解析 JSON
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return {'code': 400, 'msg': 'username or password missing'}
    
    with current_app.app_context():
        user = Users.query.filter_by(username=username).first()

        if user is None:
            return {'code': 404, 'msg': 'user not found'}

        if user.check_password(password):
            return {'code': 200, 'msg': 'login success', 'data': {'id': user.id, 'username': user.username}}
        else:
            return {'code': 401, 'msg': 'wrong password'}