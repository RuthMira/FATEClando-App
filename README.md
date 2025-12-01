python -m venv .venv
.\.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt

Pasta e nomes padrao (mesmo diretorio dos scripts):
- Sua chave publica: `chave_publica.pem`
- Sua chave privada: `chave_privada.pem`
- Chave publica do colega (copie para ca): `chave_publica_colega.pem`
- Mensagens cifradas por arquivo: `mensagem_cifrada.bin`

Fluxo:
1) Rode `python gerarChaves.py` para criar suas chaves.
2) Envie `chave_publica.pem` ao colega e receba a dele; salve como `chave_publica_colega.pem`.
3) Servidor: `python server_thread_tcp.py` (usa `chave_privada.pem` e apenas decifra/mostra o que recebe).
4) Cliente: `python client_thread_tcp.py` (usa `chave_publica_colega.pem` para cifrar antes de enviar).
5) Para testar por arquivo: `python cifrarMsg.py` (cifra com `chave_publica_colega.pem`) e `python decifrarMsg.py` (decifra com `chave_privada.pem`).
