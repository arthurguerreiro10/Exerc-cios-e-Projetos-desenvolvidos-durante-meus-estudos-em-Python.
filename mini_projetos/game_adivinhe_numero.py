import random

computador = random.randint(0,10)
print('Sou seu Computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')

palpite = int(input('Qual é seu palpite?: '))
tentativas = 1

while palpite != computador:
    if palpite < computador:
        print('Mais... tente mais uma vez.')
    else:
        print('Menos... tente mais uma vez.')

    palpite = int(input('Qual é seu palpite?: '))
    tentativas += 1

print(f'Você acertou com {tentativas} tentativas. PARABÉNS!!!')
