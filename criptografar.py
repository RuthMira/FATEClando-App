#!/usr/bin/env python3
"""
criptografar.py

Criptografa uma mensagem de texto usando a chave pública RSA.
"""

import rsa


def cifrar(msg):
    """Carrega a chave pública do colega e cifra a mensagem."""
    with open(
        r"C:\Users\ruth_\OneDrive\Área de Trabalho\FATEClando-App\chave_publica_colega.pem", "rb"
    ) as arq:
        txt = arq.read()

    pub = rsa.PublicKey.load_pkcs1(txt, format="PEM")

    if isinstance(msg, str):
        msg = msg.encode("utf-8")

    msgc = rsa.encrypt(msg, pub)
    return msgc
