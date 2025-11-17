#!/usr/bin/env python3
"""
Cliente TCP simples que envia mensagens cifradas usando o helper `cifrar`.
"""

import socket
from threading import Thread

from criptografar import cifrar

global tcp_con


def receber():
    global tcp_con
    while True:
        msg = tcp_con.recv(1024)
        print("Server:", msg)


def enviar():
    global tcp_con
    print("Para sair use CTRL+X\n")
    msg = input()
    msgc = cifrar(msg)
    while msg != "\x18":
        tcp_con.send(msgc)
        msg = input()
        msgc = cifrar(msg)
    tcp_con.close()


SERVER = "172.20.10.4"
PORT = 5000

tcp_con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (SERVER, PORT)
tcp_con.connect(dest)

t_rec = Thread(target=receber, args=())
t_rec.start()

t_env = Thread(target=enviar, args=())
t_env.start()
