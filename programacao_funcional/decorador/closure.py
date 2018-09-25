def fabrica_de_multiplicadores(multiplicador):
    def multiplicar(n):
        return n * multiplicador

    return multiplicar


dobro = fabrica_de_multiplicadores(2)
triplo = fabrica_de_multiplicadores(3)
print(dobro(3))
print(triplo(4))
