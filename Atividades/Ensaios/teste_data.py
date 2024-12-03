'''

import datetime 

dia_i = int(input('Digite o dia inicial: '))
mes_i = int(input('Digite o mês inicial: '))
dia_f = int(input('Digite o dia final: '))
mes_f = int(input('Digite o mês final: '))




data_i = datetime.date(2012,mes_i,dia_i)
data_f = datetime.date(2012,mes_f,dia_f)

dias_corridos = datetime.timedelta(days=dia_f - dia_i)

print(dias_corridos)
'''

h_incial = int(input('Informe a hora inicial da partida: '))
min_inicial = int(input('informe os minutos iniciais da partida: '))

h_final = int(input('Informe a hora final da partida: '))
min_final = int(input('informe os minutos finais da partida: '))

seg_inicial = ((h_incial * 60) + min_inicial) * 60
seg_final = ((h_final * 60) + min_final) * 60

a = ((seg_final - seg_inicial) / 60) / 60

print(a)

