import operator

alunos = [('Renzo', 0), ('Luciano', 10), ('Ada', 9)]

print([nome for nome, nota in alunos if nota > 5])


def possui_nota_maior_que_5(aluno):
    _, nota = aluno
    return nota > 5


print(list(filter(possui_nota_maior_que_5, alunos)))

print(list(map(operator.itemgetter(0), filter(possui_nota_maior_que_5, alunos))))
