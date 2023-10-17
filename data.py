#bibliotecas importadas
from datetime import datetime, date
#apresentação
print('\n\t\t\t --Verificador de Estação--\n')
print('Digite a data do seu nascimento')
year = int(input('Digite o ano: '))
month = int(input('Digite o mês: '))
day = int(input('Digite o dia: '))
data = datetime(year,month,day)
season = [datetime(year,3,20),datetime(year,6,21),
          datetime(year,9,23),datetime(year,12,22),
          datetime(year+1,3,20)]
#
if data > season[0] and data < season[1]:
    print('Você nasceu no Outono')
elif data > season[1] and data < season[2]:
    print('Você nasceu no  Inverno')
elif data > season[2] and data < season[3]:
    print('Você nasceu na Primavera')
else:
    print('Você nasceu no Verão')


