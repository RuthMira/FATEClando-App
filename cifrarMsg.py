from pathlib import Path
import rsa

# Usa a chave publica do colega para cifrar uma mensagem digitada.
PASTA = Path(__file__).resolve().parent
ARQ_CHAVE_COLEGA = PASTA / "chave_publica_colega.pem"  # copie aqui a chave publica recebida
ARQ_MSG = PASTA / "mensagem_cifrada.bin"

print(" \\-------------------------------//")
print(" **Prj Banco de Dados Distribuidos**")
print(" \\-------------------------------//")
print("Cifrador de mensagens (arquivos padrao no mesmo diretorio)")

mensagem = input("Mensagem a ser cifrada: ").encode("utf-8")
if not ARQ_CHAVE_COLEGA.exists():
    raise FileNotFoundError(f"Chave publica do colega nao encontrada: {ARQ_CHAVE_COLEGA}")

chave_publica = rsa.PublicKey.load_pkcs1(ARQ_CHAVE_COLEGA.read_bytes(), format="PEM")
mensagem_cifrada = rsa.encrypt(mensagem, chave_publica)

ARQ_MSG.write_bytes(mensagem_cifrada)
print(f"Mensagem cifrada salva em {ARQ_MSG}")
