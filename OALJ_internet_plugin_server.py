#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from multiprocessing import Process
import os
import time
import socket
import fileinput

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
local_ip=input('Please enter the ipv4 of this server: ')
s.bind((local_ip,2334))
s.listen(10)
usend=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


def solve(sock,addr):
    print('connect from',addr[0])
    filename=sock.recv(1024).decode('utf-8')
    pro_num=sock.recv(1024).decode('utf-8')
    time.sleep(0.3)
    linenumber=sock.recv(1024).decode('utf-8')
    sock.send(addr[0].encode())
    print("filename:",filename)
    print('problem number:',pro_num)
    print('linenumber:',linenumber)
    textfile=open('./%s'%filename,'w')
    i=1
    l=int(linenumber)
    while i<l-1 :
        i+=1
        temp=sock.recv(1024).decode('utf-8')
        textfile.write(temp)
    textfile.close()
    print('successfully receive from',addr[0])
    os.system('oalj -q > temp.txt')
    resfile=open('./temp.txt','r')
    data=resfile.read()
    sock.send(data.encode())
    #while True:
    send(addr[0],data)
    quit()


def send(addr,data):
    usend.sendto(data.encode(),(addr,1027))


print('waiting ...')
while True:
    sock,addr=s.accept()
    p=Process(target=solve,args=(sock,addr))
    p.start()
