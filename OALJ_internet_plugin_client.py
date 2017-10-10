#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Process
import os
import socket
import time
import fileinput

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=input('please enter the ip of server: ')
s.connect((ip,2334))
temp=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


def udpget():
    temp.bind((myaddr,1027))
    data,addr=temp.recvfrom(1024)
    print('resault: ',data.decode('utf-8'))



filename=input('please enter the name of file: ')
pro_num=input('please enter the problem number: ')
textfile=open('%s'%filename,'r')
i=0
while True:
    line=textfile.readline()
    if not line:
        break
    i=i+1
c=str(i)
s.send(filename.encode())
s.send(pro_num.encode())
time.sleep(0.3)
s.send(c.encode())
myaddr=s.recv(1024).decode('utf-8')
print(myaddr)
textfile.close()
textfile=open('./%s'%filename,'r')
for line in textfile:
    s.send(line.encode())
print('get it!')
s.close()
p=Process(target=udpget,args=())
p.start()
quit()
