from functools import wraps
from time import sleep, strftime


def logar(f):
    @wraps(f)
    def executar_com_tempo(*arg, **kwargs):
        print(strftime('%H:%M:%S'))
        return f(*arg, **kwargs)

    return executar_com_tempo


@logar
def mochileiro():
    return 42


@logar
def ola(nome):
    return f'Olá {nome}'


if __name__ == '__main__':
    print(mochileiro())
    print(mochileiro.__name__)
    print(ola('Renzo'))
    print(ola.__name__)
    sleep(1)
    print(mochileiro())
    print(ola('Luciano'))
