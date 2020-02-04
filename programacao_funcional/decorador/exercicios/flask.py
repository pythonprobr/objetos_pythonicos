"""
>>> app = Flask()
>>> set(app.rotas)
set()
>>> @app.rota('/')
... def raiz():
...     return 'raiz'
...
>>> set(app.rotas)
{'/'}
>>> raiz()
'raiz'
>>> app.executar('/')
'raiz'
>>> @app.rota('/nome')
... def nome(usuario):
...     return f'Nome: {usuario}'
...
>>> list(app.rotas)
['/', '/nome']
>>> nome('Python')
'Nome: Python'
>>> app.executar('/nome', 'Pro')
'Nome: Pro'
>>> app.executar('/nao_existe')
404

"""
from decorator import decorate


class Flask:
    def __init__(self):
        self.rotas = dict()

    def rota(self, path):
        def execute_f(func, *args, **kwargs):
            return func(*args, **kwargs)

        def decorator(f):
            self.rotas[path] = f
            return decorate(f, execute_f)

        return decorator

    def executar(self, path, *args, **kwargs):
        if path not in self.rotas:
            return 404
        f = self.rotas[path]
        return f(*args, **kwargs)
