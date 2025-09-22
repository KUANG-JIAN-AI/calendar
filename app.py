from flask import Flask
from config import Config
from app.models import db
from app.routes import register_routes

app = Flask(__name__)
app.config.from_object(Config)

# 初始化数据库
db.init_app(app)

# 注册路由
register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
