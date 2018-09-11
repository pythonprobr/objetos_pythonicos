"""
>>> def ola():
...     print('Olá')
...
>>> executar(ola)
Olá
>>> executar(ola, 2)
Olá
Olá
>>> def ola_mundo():
...     print('Olá Mundo')
...
>>> executar(ola_mundo, 3)
Olá Mundo
Olá Mundo
Olá Mundo
"""


def executar(f, n=1):
    for _ in range(n):
        f()
