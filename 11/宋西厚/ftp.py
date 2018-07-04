import socketserver,json,os
from pathlib import Path

#创建自己的 handler
class Myhandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                if not self.data:
                    raise ConnectionResetError("远程主机强迫关闭了一个现有的连接")

                self.datadic = json.loads(self.data.decode())  #拿到数据字典
                print("主机{},链接成功".format(self.client_address))

                self.cmd = self.datadic["cmd"]
                self.filename = self.datadic["filename"]
                self.path = self.datadic["path"]
                # 发过来的 数据json {"cmd":"get","filename":"abc.txt","path":"c:/"}
                # 拿到命令
                if hasattr(self,self.cmd):
                    fnn = getattr(self,self.cmd)
                    fnn(self.filename,self.path,self.request)

            except ConnectionResetError as e:
                print("Error:",e)
                break

    # 发过来的 数据格式 json {"cmd":"get","filename":"abc.txt","path":"c:/"}
    #下载
    def get(self,fliename,path,conn):
        paths = os.path.join(path,fliename)
        p = Path(paths)

        if p.is_file():
            with open(p,"r") as f:
                conn.send(f.read().encode())
                print ("下载成功")
            print("file",p)
        #访问目录
        if p.is_dir():
            dic = []
            for k in p.iterdir():
                dic.append(str(k))
            data = json.dumps(dic)
            conn.send(data.encode())

    DOWNLOADPATH = "C:/downloads/"  # 固定的保存位置
    #上传
    def put(self,fliename,path,conn):  #上传的时候  path 是文件名  上传的统一路径 c:/downloads
        with open("{}{}".format('C:/downloads/',path),"w") as f:
            f.write(fliename)
            conn.send("上传成功".encode())

if __name__ == "__main__":
    addr = ('127.0.0.1',8088)
    sock = socketserver.ThreadingTCPServer(addr,Myhandler)
    print("等待链接...")
    sock.serve_forever()
