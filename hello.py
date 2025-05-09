#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.
Como usar:

Tenha a variavel LANG devidamente configurada ex:

	export LANG=pt-BR
Execução:
	python3 hello.py

"""
__version__ = "0.0.1"
__author__ = "Juliano Tabanez"
__license__ = "Unlicense"

import os

current_lang = os.getenv("LANG")[:5]


msg = "Hello, World!"

if current_lang == "pt_BR":
   msg = "Olá, Mundo!"
elif current_lang == "it_IT":
   msg = "Ciao, Mondo!"

print(msg)

