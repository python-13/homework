import socket,json
from pathlib import Path



class ClientFtp:
    DOWNLOADPATH = "e:/"
    def __init__(self,ip,prot):
        self.addr = (ip,prot)
        self.sock = socket.socket()

    def start(self):
        self.sock.connect(self.addr)
        while True:
            print("输入你的命令，格式(get filename path 或者 put filename path)>>>")
            cmds = input(">>>")
            cmd,filename,path = cmds.split()
            if hasattr(self,cmd):
                fn = getattr(self,cmd)
                fn(filename,path)
                break
    #上传
    def get(self,filename,path):
        filepath = "{}{}".format(path,filename)
        p = Path(filepath)
        dic = {
            "cmd": "get",
            "filename": filename,
            "path": path
        }
        data = json.dumps(dic).encode()
        self.sock.send(data)
        if p.is_file():
            loaddata = self.sock.recv(1024).decode()
            with open("{}{}".format(self.DOWNLOADPATH,filename),"w") as f:
                f.write(loaddata)
                print("下载成功")
            self.sock.close()

        if p.is_dir():
            loaddata = self.sock.recv(1024).decode()
            print(loaddata)

    #下载
    def put(self,filename,path):
        p = Path("{}{}".format(path,filename))
        with open(p,"r") as f:
            dic = {
                "cmd": "put",
                "filename": f.read(),
                "path": filename  #上传的时候  path 是文件名
            }
            data = json.dumps(dic).encode()
            self.sock.send(data)
            data = self.sock.recv(1024).decode()
            print(data)
            self.sock.close()

if __name__ == "__main__":
    sk = ClientFtp('127.0.0.1',8088)
    sk.start()

