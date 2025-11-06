# FATEClando App – Chat TCP com RSA (Assimétrico)

Trabalho: chat TCP/IP ponta a ponta com criptografia assimétrica.

- Cada aluno gera seu par de chaves (pública/privada) localmente.
- Troca-se APENAS a chave pública com o colega (manual: por arquivo, e-mail ou commit). Nunca compartilhe a chave privada.
- Toda mensagem enviada é cifrada com a chave pública do DESTINATÁRIO.
- Quem recebe decifra automaticamente com a sua chave privada.

Arquivos principais:
- `gerar_chaves.py` – gera `chave_privada.pem` e `chave_publica.pem`.
- `tcp_server.py` – lado servidor do chat.
- `tcp_client.py` – lado cliente do chat.
- `rsa_utils.py` – utilitários de criptografia.

## 1) Gerar suas chaves
```
python gerar_chaves.py
```

Isso cria `chave_privada.pem` (MANTENHA SECRETA) e `chave_publica.pem` (pode compartilhar).

## 2) Trocar chaves públicas (manual)
- Envie seu arquivo `chave_publica.pem` para o colega.
- Receba a chave pública do colega e salve, por exemplo, como `chave_publica_colega.pem` na mesma pasta.


## 3) Executar o chat cifrado
Escolham quem será o servidor e quem será o cliente.

Servidor (exemplo porta 5000):
```
python tcp_server.py --port 5000 \
  --my-private chave_privada.pem \
  --peer-public chave_publica_colega.pem
```

Cliente (informar IP/porta do servidor):
```
python tcp_client.py --host 127.0.0.1 --port 5000 \
  --my-private chave_privada.pem \
  --peer-public chave_publica_colega.pem
```

Digite mensagens no prompt. Para sair, use `/quit`.

(resumo)
- Envio: mensagem → RSA-OAEP(SHA-256) com chave pública do colega → Base64 → TCP.
- Recepção: Base64 → RSA-OAEP com sua chave privada → texto claro.
- Código-fonte (estes arquivos) + prints da execução (ambos os lados).
