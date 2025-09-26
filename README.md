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

打包成 .exe 文件
pip install flask pywebview pyinstaller

新建一个 main.py
import threading
from app import create_app
import webview

def run_flask():
    app = create_app()
    app.run(port=5000)

if __name__ == "__main__":
    # 在子线程启动 Flask
    t = threading.Thread(target=run_flask)
    t.daemon = True
    t.start()

    # 启动桌面窗口，加载本地服务
    webview.create_window("日程管理", "http://127.0.0.1:5000")
    webview.start()

执行打包操作
pyinstaller --onefile --noconsole main.py

