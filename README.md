创建虚拟环境
py -3 -m venv .venv

进入虚拟环境
.venv\Scripts\activate

安装 flask 框架
pip install flask

目录结构
calendar/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── controllers/
│   │   └── user.py
│   ├── models/
│   │   └── user.py
│   ├── templates/
│   │   ├── index.html
│   └── static/
│       ├── css/
│       └── js/
├── config.py
├── app.py
└── run.py