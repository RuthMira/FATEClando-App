from pathlib import Path
import rsa

# Gera automaticamente um par RSA e salva ao lado do script.
TAMANHO_CHAVE = 2048
BASE_DIR = Path(__file__).resolve().parent
ARQ_CHAVE_PUB = BASE_DIR / "chave_publica.pem"
ARQ_CHAVE_PRI = BASE_DIR / "chave_privada.pem"

print(" \\-------------------------------//")
print(" **Prj Banco de Dados Distribuidos**")
print(" \\-------------------------------//")
print("Gerador de chaves assimetricas")
print(f"Tamanho usado: {TAMANHO_CHAVE} bits")

publica, privada = rsa.newkeys(TAMANHO_CHAVE)

ARQ_CHAVE_PUB.write_bytes(publica.save_pkcs1(format="PEM"))
ARQ_CHAVE_PRI.write_bytes(privada.save_pkcs1(format="PEM"))

print("Chaves geradas com sucesso.")
print(f"Publica:  {ARQ_CHAVE_PUB}")
print(f"Privada:  {ARQ_CHAVE_PRI}")
print("\nCopie a chave publica para o colega e mantenha a privada somente com voce.")
