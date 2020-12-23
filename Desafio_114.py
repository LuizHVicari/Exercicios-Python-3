# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
# Assisti o começo da resolução do exercício para descobrir qual biblioteca usar para tentar acessar o site

import urllib
import urllib.request

try:
    urllib.request.urlopen('http://pudim.com.br/')
except:
    print('O site não está disponível')
else:
    print('O site está disponível')