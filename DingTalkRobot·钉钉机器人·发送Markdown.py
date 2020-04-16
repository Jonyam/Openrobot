#配置演示：https://www.bilibili.com/video/BV195411t71E
###导入模块
import requests
from lxml import etree
import requests,json
import time
from os import*
import os
import random
url = 'url'  #你的钉钉机器人webhook地址
s = input('请输入您要发送的内容\n')
program = {
    "msgtype": "markdown",#标记为MarkDown
    "markdown": {
        "title":"您的好友使用JROBOT(DingTalk)发来一条信息",
        "text": s+''#MarkDown编写的语言
        },
}

headers = {'Content-Type': 'application/json'}
f = requests.post(url, data=json.dumps(program), headers=headers)

