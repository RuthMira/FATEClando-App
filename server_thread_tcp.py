# Servidor TCP que somente decifra e exibe mensagens recebidas
import base64
from pathlib import Path
import socket
import rsa

global tcp_con

ARQ_CHAVE_PRI = Path(__file__).resolve().parent / "chave_privada.pem"


def carregar_chave_privada():
    if not ARQ_CHAVE_PRI.exists():
        raise FileNotFoundError(f"Chave privada nao encontrada: {ARQ_CHAVE_PRI}")
    return rsa.PrivateKey.load_pkcs1(ARQ_CHAVE_PRI.read_bytes(), format="PEM")


def receber(chave_privada):
    global tcp_con
    while True:
        msg = tcp_con.recv(4096)
        if not msg:
            break
        try:
            cifrada = base64.b64decode(msg, validate=True)
            decifrada = rsa.decrypt(cifrada, chave_privada).decode("utf-8")
            print("Cliente (decifrada):", decifrada)
        except Exception:
            print("Cliente (bruta):", msg)


# Endereco IP do Servidor
HOST = ""

# Porta que o Servidor vai escutar
PORT = 5002

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

chave_privada = carregar_chave_privada()

while True:
    tcp_con, cliente = tcp.accept()
    print("Concetado por ", cliente)
    receber(chave_privada)
    print("Finalizando conexao do cliente", cliente)
    tcp_con.close()
