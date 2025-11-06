#!/usr/bin/env python3
"""
criptografar.py

Criptografa uma mensagem de texto usando a chave pública RSA.
"""

from rsa_utils import load_public_key, rsa_encrypt
import base64


def criptografar_mensagem(mensagem: str, public_key_path: str = "chave_publica.pem"):
    chave_publica = load_public_key(public_key_path)
    mensagem_bytes = mensagem.encode("utf-8")
    mensagem_cifrada = rsa_encrypt(chave_publica, mensagem_bytes)

    with open("mensagem_cifrada.txt", "wb") as f:
        f.write(mensagem_cifrada)

    print("Mensagem criptografada com sucesso!")
    print("  - Arquivo gerado: mensagem_cifrada.txt")
    print("  - Visualização base64:")
    print(base64.b64encode(mensagem_cifrada).decode())


if __name__ == "__main__":
    mensagem = input("Digite a mensagem para criptografar: ")
    criptografar_mensagem(mensagem)

