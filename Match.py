opcao_escolhida = int(input('Digite um valor'))
match opcao_escolhida:
    case 1:
        print('Adicionar restaurante')
    case 2:
        print('Listar restaurantes')
    case 3:
        print('Ativar restaurante')
    case 4:
        print('Finalizar app')
    case _:
        print('Opção inválida')
# match pode ser usado para de uma maneira sinplificado no lugar do if, elif e else