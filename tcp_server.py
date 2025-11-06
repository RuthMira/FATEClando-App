#!/usr/bin/env python3
"""
Servidor de chat TCP com criptografia ponta a ponta (RSA).

- Cada mensagem enviada é cifrada com a CHAVE PÚBLICA do colega (peer).
- Mensagens recebidas são decifradas com a sua CHAVE PRIVADA.

Execução exemplo:
  python tcp_server.py --port 5000 \
      --my-private chave_privada.pem \
      --peer-public chave_publica_colega.pem

No colega (cliente): ver tcp_client.py
"""

from __future__ import annotations

import argparse
import base64
import socket
import threading
import sys
from rsa_utils import load_private_key, load_public_key, rsa_encrypt, rsa_decrypt


def receiver_loop(sock: socket.socket, my_private_path: str):
    priv = load_private_key(my_private_path)
    f = sock.makefile("rb")
    try:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                ct = base64.b64decode(line)
                pt = rsa_decrypt(priv, ct)
                print(f"\n[Peer]: {pt.decode('utf-8', errors='replace')}")
                print("> ", end="", flush=True)
            except Exception as e:
                print(f"\n[Erro ao decifrar]: {e}")
                print("> ", end="", flush=True)
    finally:
        f.close()


def main():
    ap = argparse.ArgumentParser(description="Servidor de chat TCP cifrado com RSA")
    ap.add_argument("--host", default="0.0.0.0", help="Endereço para escutar (default 0.0.0.0)")
    ap.add_argument("--port", type=int, default=5000, help="Porta (default 5000)")
    ap.add_argument("--my-private", required=True, dest="my_private", help="Caminho da sua chave privada .pem")
    ap.add_argument("--peer-public", required=True, dest="peer_public", help="Caminho da chave pública do colega .pem")
    args = ap.parse_args()

    peer_pub = load_public_key(args.peer_public)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
        srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv.bind((args.host, args.port))
        srv.listen(1)
        print(f"[Servidor] Aguardando conexão em {args.host}:{args.port}...")
        conn, addr = srv.accept()
        print(f"[Servidor] Conectado por {addr[0]}:{addr[1]}")

        t = threading.Thread(target=receiver_loop, args=(conn, args.my_private), daemon=True)
        t.start()

        try:
            f = conn.makefile("wb")
            while True:
                try:
                    msg = input("> ")
                except EOFError:
                    break
                if msg.strip().lower() in {"/quit", ":q", "\x04"}:
                    break
                ct = rsa_encrypt(peer_pub, msg.encode("utf-8"))
                b64 = base64.b64encode(ct) + b"\n"
                f.write(b64)
                f.flush()
        finally:
            try:
                conn.shutdown(socket.SHUT_RDWR)
            except Exception:
                pass
            conn.close()
            print("[Servidor] Conexão encerrada.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[Servidor] Finalizado por usuário.")

