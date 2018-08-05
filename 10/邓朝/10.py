import requests

urls = ['http://www.baidu.com', 'http://www.163.com', 'http://www.qq.com']


def geturl():
    yield from urls


def status(p):
    while True:
        try:
            url = next(p)
            ret = requests.get(url)
            status = 'url->{} status->{}'.format(url, ret.status_code)
            print(status)
        except StopIteration:
            break


status(geturl())
