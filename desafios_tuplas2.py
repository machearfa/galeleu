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

print("prod. entregues")
for i in pedidos:
    if i[3] == 'Entregue':
        valores_entregues.append(i[2])
        print(f' {i[0].center(40, '-')}')

print()
print('valor total dos entregues', sum(valores_entregues))

if i[1] == 'Vestuário' and i[-1] == 'Cancelado':
    contador += 1 
    print()
    print('produtos da categoria vestuario cancelados: ',contador)
    print()
categoria_para_filtrar = input('digite uma categoria para filtrar :')


print('pedidos da categoria', categoria_para_filtrar)
for item in pedidos:
    if categoria_para_filtrar.lower() == item[1].lower():
        print(f'- {item[0]}')