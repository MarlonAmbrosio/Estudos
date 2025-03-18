from random import randint

aposta_contador = 0
lista = ['Manga', 'Uvaia', 'Melão', 'Amora']

valor = 100

start = int(input('Press 1 to start: '))
while start != 1:
    break
while start == 1:
    if valor <= 0:
        print(f'Você ficou sem saldo, R${valor}, não pode continuar jogando!')
        break
    apostar = float(input('Quanto vai apostar?: R$'))
    while apostar > valor:
        apostar = float(input('Valor muito alto, tente novamente: R$'))

    escolha = input('[Apostar] ou [Sair]').upper()

    while escolha != 'APOSTAR' and escolha != 'SAIR':
        escolha = input('[Apostar] ou [Sair]').upper()

    while escolha == 'APOSTAR' and aposta_contador < 1:
        n1 = lista[randint(0, 3)]
        n2 = lista[randint(0, 3)]
        n3 = lista[randint(0, 3)]

        valor = valor - apostar
        aposta_contador += 1

        if n1 == n2 and n2 == n3:
            premio = apostar * 3
            valor += premio
            print(f'Parabéns! Você ganhou {premio}, seu saldo agora é de R${valor}')
            print(n1, n2, n3)
        else:
            print(f'Você perdeu! R${apostar}, seu saldo agora é de R${valor}')
            print(n1, n2, n3)

    aposta_contador -= 1
    if escolha == 'SAIR':
        print(f'Jogo finalizado! Seu saldo foi de R${valor}')
        break