def fabrica_de_multiplicadores():
    def dobro(n):
        return n * 2

    return dobro


dobro_externo = fabrica_de_multiplicadores()
dobro_externo_2 = fabrica_de_multiplicadores()
print(dobro_externo is dobro_externo_2)
print(dobro_externo(3))
