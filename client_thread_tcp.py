# Cliente TCP com cifragem RSA ao enviar
import base64
from pathlib import Path
import socket
from threading import Thread
import rsa

global tcp_con

# Unico arquivo esperado: chave publica do servidor/colega no mesmo diretorio
ARQ_CHAVE_PUB_COLEGA = Path(__file__).resolve().parent / "chave_publica_colega.pem"


def carregar_chave_publica():
    if not ARQ_CHAVE_PUB_COLEGA.exists():
        raise FileNotFoundError(f"Chave publica do colega nao encontrada: {ARQ_CHAVE_PUB_COLEGA}")
    return rsa.PublicKey.load_pkcs1(ARQ_CHAVE_PUB_COLEGA.read_bytes(), format="PEM")


def receber():
    global tcp_con
    while True:
        msg = tcp_con.recv(4096)
        if not msg:
            break
        try:
            print("Server:", msg.decode("utf-8", errors="ignore"))
        except Exception:
            print("Server:", msg)


def enviar():
    global tcp_con
    chave_publica = carregar_chave_publica()
    print("Para sair use CTRL+X\n")
    msg = input()
    while msg != "\x18":
        cifrada = rsa.encrypt(msg.encode("utf-8"), chave_publica)
        cifrada_b64 = base64.b64encode(cifrada)
        tcp_con.send(cifrada_b64)
        msg = input()
    tcp_con.close()


# Endereco IP do Servidor
SERVER = "127.0.0.1"

# Porta que o Servidor esta escutando
PORT = 5002

tcp_con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (SERVER, PORT)
tcp_con.connect(dest)

t_rec = Thread(target=receber, args=())
t_rec.start()

t_env = Thread(target=enviar, args=())
t_env.start()
