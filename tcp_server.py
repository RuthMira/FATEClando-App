#!/usr/bin/env python3
import socket
from threading import Thread

import rsa

tcp_con = None

def decifrar(msgc):
    with open("chave_privada.pem", "rb") as arq:
        pri = rsa.PrivateKey.load_pkcs1(arq.read(), format="PEM")
    print("Mensagem cifrada:", msgc.hex())
    msg = rsa.decrypt(msgc, pri)
    print("Mensagem decifrada:", msg.decode("utf-8"))


def cifrar(msg):
    with open("chave_publica_colega.pem", "rb") as arq:
        pub = rsa.PublicKey.load_pkcs1(arq.read(), format="PEM")
    return rsa.encrypt(msg.encode("utf-8"), pub)


def enviar():
    global tcp_con
    while True:
        msg = input()
        if not msg:
            continue
        msgc = cifrar(msg)
        tcp_con.send(msgc)


HOST = ""
PORT = 5000
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind((HOST, PORT))
tcp.listen(1)
print("Servidor escutando em", HOST or "0.0.0.0", "na porta", PORT)

while True:
    tcp_con, cliente = tcp.accept()
    print("Conectado por", cliente)
    t_env = Thread(target=enviar)
    t_env.start()
    while True:
        msg = tcp_con.recv(1024)
        if not msg:
            break
        decifrar(msg)
    print("Finalizando conexao do cliente", cliente)
    tcp_con.close()
