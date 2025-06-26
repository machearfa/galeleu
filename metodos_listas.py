#Metodo .append(elemento a adicionar) , adiciona um elemento no final da lista

lista_frutas = ['banana', 'maçã', 'morango']

lista_frutas.append('kiwi')

#metodo insert, adiciona um elemento em uma posição especificada

lista_frutas.insert(2, 'pera')

lista_frutas.insert(0, 'laranja')


lista_frutas.remove('banana') #remove um elemento especificado
print(lista_frutas)

lista_idades = [33, 11, 13, 19, 42]
lista_idades.sort()
print(lista_idades)
lista_idades.sort(reverse=True)
print(lista_idades)

lista_frutas2 = ['banana', 'maçã', 'morango', 'banana', 'banana']

print(lista_frutas2.count('banana'))
print(lista_frutas2)