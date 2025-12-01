from pathlib import Path
import rsa

# Decifra a mensagem cifrada com a chave privada local.
PASTA = Path(__file__).resolve().parent
ARQ_CHAVE_PRI = PASTA / "chave_privada.pem"
ARQ_MSG = PASTA / "mensagem_cifrada.bin"

print(" \\-------------------------------//")
print(" **Prj Banco de Dados Distribuidos**")
print(" \\-------------------------------//")
print("Decifrador de mensagens (arquivos padrao no mesmo diretorio)")

if not ARQ_CHAVE_PRI.exists():
    raise FileNotFoundError(f"Chave privada nao encontrada: {ARQ_CHAVE_PRI}")
if not ARQ_MSG.exists():
    raise FileNotFoundError(f"Arquivo de mensagem nao encontrado: {ARQ_MSG}")

chave_privada = rsa.PrivateKey.load_pkcs1(ARQ_CHAVE_PRI.read_bytes(), format="PEM")
mensagem_cifrada = ARQ_MSG.read_bytes()

mensagem = rsa.decrypt(mensagem_cifrada, chave_privada)
print(f"Mensagem decifrada: {mensagem.decode('utf-8')}")
