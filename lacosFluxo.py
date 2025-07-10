notas = [
    ['ana', [8, 7, 9]],
    ['carlos', [5, 6, 7]],
    ['joão', [10, 9, 6]]
]


for aluno in notas:
    nome = aluno[0]
    notas = aluno[1]
    soma = sum(notas) / len(notas)
    print(f'a nota do(a) {aluno[0]} é {soma}')