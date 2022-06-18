import os.path
import time

from flask import Flask, render_template, request, redirect  # 第三方模块 Python中轻量级的web框架

# 创建一个app
app = Flask(__name__)


# 常用的网络请求get获取服务器的内容   post向服务器提交内容

# 通过route(‘网址’)绑定一个网址
# 默认情况下只处理get请求  method 声明即处理POST请求也处理GET请求
@app.route('/index', methods=('POST', 'GET'))
def index():
    # 如果用户发起get请求直接渲染网页给浏览器
    if request.method == 'GET':
        # 如果不存在info.txt 则创建一个文件
        if not os.path.exists('info.txt'):
            open('info.txt', 'w')
        # 读取info.txt 获取用户提交的留言
        with open('info.txt', 'r') as f:
            data = f.readlines()
        return render_template('index.html', data=data)
    # 如果用户发起的是一个POST请求，获取用户提交的留言内容
    elif request.method == "POST":
        # 获取用户提交的留言内容
        message = request.form.get('message')
        # 如果用户没有输入空，才执行保存的操作
        if message:
            # 将用户提交的留言保存到服务器
            message_time = time.strftime('%Y-%m-%d %H:%M:%S')
            with open('info.txt', 'a') as f:
                f.write(message + "  " + message_time + "\n")

        else:
            return '不要什么都不写呀！'
        # 重定向到index首页
        return redirect('/index')

    # 程序从这里开始运行


if __name__ == '__main__':
    app.run()
