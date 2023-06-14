#!/usr/bin/env python3
#Linha acima, SHIBANG, mensagem enviada para o sistema(consigo forçar uma versão python para ser rodada(boa prática))

"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem correspodente.

Como usar:

Tenha a variável LANG devidamente configurada ex.:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Stefane Brito"
__license__ = "Unlicense"

import os

#current_language = "en_US"
current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, world!"

if current_language == "pt_BR":
    msg = "Olá, mundo!"
elif current_language == "it_IT":
    msg = "Ciao, mondo!"
elif current_language == "es_SP":
    msg = "Hola, mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour, monde!"

print(msg) 