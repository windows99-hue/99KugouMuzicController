# 99酷狗音乐遥控器

### [English Version]("https://github.com/windows99-hue/99KugouMuzicController/blob/main/readme-eng.md")

#### 本程序可以让您在手机、平板甚至homepod等其他终端上方便的控制电脑端的酷狗音乐，让其可以进行暂停\播放\听歌识曲等功能

## 演示视频

<video src="https://github.com/windows99-hue/99KugouMuzicController/raw/refs/heads/main/video.mp4"></video>

## 部署

#### 请使用python3部署此程序1.下载存储库，安装所需要的库

~~~bash
pip install -r requirement.txt
~~~

#### 2.修改程序

将```main.py```中的第8行

~~~python
with open(r"D:\flask_app.log", "w") as f:
~~~

路径改为您想要的路径，```flas_app.log```中存储的是flask服务器的日志文件，由于本程序在```pythonw```中运行，所以所有的控制台显示会被重定向到```flask_app.log```此文件会在程序每一次重新运行时被清空。

---------

将`main.py`中的第45行

```python
os.system("start \"\" <your path of Kugou Music>")
```

中的路径改为您`Kugou.exe`的路径。注意：如果路径中有空格，请以下面的代码作为模板

~~~python
os.system("start \"\" \"<your path of Kugou Music>\"")
~~~

将`<your path of Kugou Music>`替换为你的酷狗音乐的路径

---------

将```main.py```中的第101行

~~~python
app.run(host="0.0.0.0", debug=False, port=52099)
~~~

中的```port```参数改为您想让flask服务器运行的端口，默认为52099端口，不要忘了在防火墙中允许您更改后的端口

----------------

#### 3.修改bat文件

将```start_server.bat```

~~~bat
start "" pythonw -u "<your path of main.py>"
~~~

中的`<your path of main.py>`改为`main.py`的绝对路径

您可以把`start_server.bat`放入`C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup`中，这可以让`start_server.bat`开机自启动

---------

#### 4.安装apk文件

将```99KugouMusicController.apk`安装到终端即可

--------------

#### 5.修改快捷键

1. 启动酷狗音乐，进入设置，热键设置
2. 在`快捷键设置`中勾选`启用全局快捷键`
3. 按照图片修改快捷键

![热键设置](E:\99之没事写的小程序\homepod\控制电脑\01-github\99KugouMuzicController\hotkey.png)

如果我设置的快捷键与您的冲突，您可以更改`main.py`中第43~第87行的所有快捷键，例如：

~~~python
elif(q == "stoporstart"):
    hk("alt", "n")
~~~

或

~~~python
elif(q == "fastforward"):
    if not qp:
        return "Cannot Found Args Called qp"
~~~

## 运行

通过`start_server.bat`启动服务端，建议在首次启动时通过

~~~bash
python main.py
~~~

运行以检查错误

首次启动时，请在app中更改服务端地址`<your ip>:<your port>`

您可以在更改完完成后尝试每个选项，有的选项需要附加参数，在快进\快退中，附加参数代表快进\快退的时间，单位为秒；在音量加\音量减中，附加参数代表音量加\音量减的大小，单位为百分比。

## 使用声明

本程序使用MIT协议，其中的算法仍有缺陷，以后可能会更新，此程序也适配其他软件，因为原理是热键，之后我可能会开源app，敬请期待。
