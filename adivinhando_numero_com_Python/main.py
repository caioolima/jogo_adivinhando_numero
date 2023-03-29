import random

print('Olá, seja bem - vindo ao jogo da adivinhação !')

def GerandoNumero():
    return random.randint(1,100)
def Adivinhando():
    resultado = GerandoNumero()
    chances = 0
    print('\nJogo iniciado!')
    adivinhando = 0
    while adivinhando is not resultado:
        chances +=1
        adivinhando = int(input('\nQual número você acha que é: '))
        if adivinhando > resultado:
            print('Errou... A resposta certa é menor que',adivinhando)
        elif adivinhando < resultado:
            print('Errou... A resposta certa é maior que', adivinhando)
        else:
            print('Você acertou, parabéns ! A resposta certa é: ', resultado,'\nApós', chances, 'tentativa (as) você conseguiu !')
            break
def Menu():
    menu = """\n--- MENU ---

1- Gerar número
2 - Adivinhar número
3 - Sair
    
ESCOLHA: """
    while True:
        escolha = input(menu)
        if escolha == '1':
            print('\nNúmero gerado...')
            GerandoNumero()
        elif escolha == '2':
            Adivinhando()
        elif escolha == '3':
            print('Você decidiu sair, até logo...')
            exit()
        else:
            print('Opção inválida, tente novamente !')
Menu()

