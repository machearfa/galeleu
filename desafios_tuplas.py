estoque = (
    ('mouse LG Tech', 10),
    ('mic Hiper x', 5),
    ('acer Nitro 5', 3),
    ('webcam HD', 0)
)

print('produtos com menos de 5 unidades em estoque')
contador = 0
soma = 0
for i in estoque: # para i (variavel) no estoque (tupla) fazer isso
    if i[1] < 5: #printa os numeros menores que 1
        print(f'-{i[0]}')
    if i[1] == 0:
        contador += 1
    
    soma += i[1]#soma cada item da tupla estoque

print('-'*50, f'a soma dos produtos é {soma}', '-'*50)