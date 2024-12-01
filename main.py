from flask import Flask, request
import pyautogui
from pyautogui import hotkey as hk
import sys
import os
import logging

with open(r"D:\flask_app.log", "w") as f:
    f.write("")

# 配置日志记录
logging.basicConfig(
    level=logging.DEBUG,  # 设置日志级别
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # 设置日志格式
    handlers=[
        logging.FileHandler(r"D:\flask_app.log"),  # 将日志写入文件
        logging.StreamHandler(sys.stdout)  # 同时也在控制台输出（可选）
    ]
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

def filter_numbers(s):
    return ''.join([char for char in s if char.isdigit()])

def shutdown_server():
    global status
    """Shuts down the Flask server."""
    status = False
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return 'Shutting down...'

@app.route('/asking')
def asking():
    t = request.args.get("type")
    q = request.args.get('q')
    qp = request.args.get('qp')
    if t:
        if t == "kugou":
            if q == "startheapp":
                os.system("start \"\" <your path of Kugou Music>")
            elif(q == "stoporstart"):
                hk("alt", "n")

            elif(q == "prev"):
                hk("alt", "left")
            elif(q == "next"):
                hk("alt", "right")

            elif(q == "silence"):
                hk("ctrl", "alt", "s")

            elif(q == "desktop_song_text"):
                hk("ctrl", "alt", "d")

            elif(q == "fastforward"):
                if not qp:
                    return "Cannot Found Args Called qp"
                qp = int(int(filter_numbers(qp)) / 3)
                for i in range(qp):
                    pyautogui.hotkey('ctrl', 'shift', 'l')
            elif(q == "fastback"):
                if not qp:
                    return "Cannot Found Args Called qp"
                qp = int(int(filter_numbers(qp)) / 3)
                for i in range(qp):
                    pyautogui.hotkey('ctrl', 'shift', 'j')

            elif(q == "volup"):
                if not qp:
                    return "Cannot Found Args Called qp"
                qp = int(int(filter_numbers(qp)) / 5)
                for i in range(qp):
                    pyautogui.hotkey('alt', 'up')
            elif(q == "voldown"):
                if not qp:
                    return "Cannot Found Args Called qp"
                qp = int(int(filter_numbers(qp)) / 5)
                for i in range(qp):
                    pyautogui.hotkey('alt', 'down')
                
            elif(q == "listen"):
                pyautogui.hotkey('shift', 'alt', 'z')

            else:
                return "Commend Not Found."
        elif t == "system":
            if q == "shutdown":
                #shutdown_server()
                print("shutdown")
                os._exit(0)
        return "OK"
    else:
        return "Error"

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=52099)
