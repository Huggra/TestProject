# Формирование списка накопления за год
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму'))
deposit_All = [(money*per_cent['ТКБ']/100),
               (money*per_cent['СКБ']/100),
               (money*per_cent['ВТБ']/100),
               (money*per_cent['СБЕР']/100)]
deposit_Max = max(deposit_All)
print(list(map(int, deposit_All)))
print('Максимальная сумма, которую вы можете заработать —', deposit_Max)