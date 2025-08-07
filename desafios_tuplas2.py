pedidos = [
    ("Camisa", "Vestuário", 59.90, "Entregue"),
    ("Tênis", "Calçados", 199.90, "Cancelado"),
    ("Calça", "Vestuário", 89.90, "Entregue"),
    ("Fone de Ouvido", "Eletrônicos", 129.90, "Pendente"),
    ("Meia", "Vestuário", 19.90, "Entregue"),
    ("Notebook", "Eletrônicos", 3299.90, "Entregue"),
    ("Jaqueta", "Vestuário", 139.90, "Cancelado"),
]

valores_entregues = []
ultimos_3_pedidos = []
contador = 0
categoria = input('digite uma categoria para pesquisar: ')

for i in pedidos:

    if i[3] == 'Entregue':
        print(f'- {i[0]}')

    valores_entregues.append(i[2])

    if valores_entregues:
        soma_dos_valores = sum(valores_entregues) / len(valores_entregues)

    if i[3] == 'Cancelado':
        print()
        contador += 1
        print(f'pedidos cancelados: {contador}')

if categoria == 'Vestuário':
    print(i[0])

if categoria == 'Calçados':
    print(i[0])

if categoria == 'Ouvido':
    print(i[0])

if categoria == 'Eletrônicos':
    print(i[0])

ultimos_3_pedidos.append('meia')
ultimos_3_pedidos.append('notebook')
ultimos_3_pedidos.append('jaqueta')

print() #pulei uma linha

print(f'valor total dos entregues: {soma_dos_valores:.3f}')

print() #pulei uma linha

print(f'ultimos 3 pedidos: {ultimos_3_pedidos}') 