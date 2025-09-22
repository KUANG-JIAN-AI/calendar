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

db 无需重复创建，在 __init__.py 中创建后，只需要 from app import db 使用即可，或者 from .. import db  # 两个点表示上一级包，也就是 app/


无法添加默认时间
pip install tzdata

from datetime import datetime
from zoneinfo import ZoneInfo

