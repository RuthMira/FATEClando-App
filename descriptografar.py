#!/usr/bin/env python3
"""
descriptografar.py

Descriptografa a mensagem cifrada usando a chave privada RSA.
"""

from rsa_utils import load_private_key, rsa_decrypt


def descriptografar_mensagem(
    private_key_path: str = "chave_privada.pem", arquivo_mensagem: str = "mensagem_cifrada.txt"
):
    chave_privada = load_private_key(private_key_path)

    with open(arquivo_mensagem, "rb") as f:
        mensagem_cifrada = f.read()

    mensagem = rsa_decrypt(chave_privada, mensagem_cifrada)
    print("Mensagem descriptografada com sucesso!")
    print("  Conteúdo original:", mensagem.decode("utf-8"))


if __name__ == "__main__":
    descriptografar_mensagem()

