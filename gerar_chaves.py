#!/usr/bin/env python3
"""
gerar_chaves.py

Gera um par de chaves RSA (pública e privada) e salva em arquivos PEM.
"""

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


def gerar_par_chaves():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    with open("chave_privada.pem", "wb") as f:
        f.write(
            private_key.private_bytes(
                serialization.Encoding.PEM,
                serialization.PrivateFormat.PKCS8,
                serialization.NoEncryption(),
            )
        )

    with open("chave_publica.pem", "wb") as f:
        f.write(
            public_key.public_bytes(
                serialization.Encoding.PEM,
                serialization.PublicFormat.SubjectPublicKeyInfo,
            )
        )

    print("Par de chaves RSA gerado com sucesso:")
    print("  - chave_privada.pem")
    print("  - chave_publica.pem")


if __name__ == "__main__":
    gerar_par_chaves()

