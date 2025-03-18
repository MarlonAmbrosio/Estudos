print('='*30)
print('BANCO M.A'.center(30))
print('='*30)

valor = int(input('Quanto você deseja sacar? R$'))
total = valor
ced = 50
total_cedula = 0
while True:
    if total >= ced:
        total -= ced
        total_cedula += 1
    else:
        print(f'Total de {total_cedula} cedulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced ==20:
            ced = 10
        elif ced == 10:
            ced = 1
        total_cedula = 0
        if total == 0:
            break
