#classificar idade em categorias

idade = int(input('Qual sua idade? '))

def verificar_idade(idade):
    if idade < 12:
        return 'Criança'
    elif idade > 12 and idade < 18:
        return 'Adolescente'
    else:
        return 'Adulto'
resultado = verificar_idade(idade)
print(f'A sua idade é {idade} e voce é {resultado}')