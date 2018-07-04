#/usr/bin/env python

# 将下面简单的多线程改用简单的协程实现，必须使用yield

import threading
import requests
import time


def status(url):
    ret = requests.get(url)
    status = "url -> {}, status -> {}".format(url, ret)
    time.sleep(1)
    print(status)


for x in ['http://baidu.com', 'http://www.163.com', 'http://www.qq.com']:
    threading.Thread(target=status, args=(x,)).start()

################################################################
    
def gen(job):

    while True:
        arg = yield ''
        if arg is None:
            return
        job(arg)


g = gen(status)
g.send(None)
g.send('http://baidu.com')
g.send('http://163.com')
g.send('http://qq.com')
