#Exercicios

#Solicite ao usuário que insira um numero e em seguida,
#use uma estrutura if else para determinar se o numero é par ou impar.

numero = int(input('Digite um numero: '))

def verificar_paridade(numero):
    if numero % 2 == 0:
        return 'par'
    else:
        return 'impar'
resultado = verificar_paridade(numero)
print(f'O numero {numero} é {resultado}.')


