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
