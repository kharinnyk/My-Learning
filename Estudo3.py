#1 - Crie uma lista para cada informação a seguir:

#Lista de números de 1 a 10;
#Lista com quatro nomes;
#Lista com o ano que você nasceu e o ano atual.

lista = [1,2,3,4,5,6,7,8,9,10]
print(lista)

lista = list(range(1, 11))
print(lista)

nomes = ['Kharinny', 'Ruan', 'Andy', 'Julinha']
print(nomes)

date = ['1997','2025' ]
print(date)

#2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

lista = []
for numero in range(1,21):
    lista.append(numero)
print(lista)