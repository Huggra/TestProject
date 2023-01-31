all_ticket = int(input("Введите количество билетов"))
youg_age = int(input("Сколько слушателей менее 18 лет?"))
midle_age = int(input("Сколько слушателей от 18 до 25 лет?"))
other_age = int(input("Сколько слушателей старше 25 лет?"))
sale = 10
if youg_age > 0:
    youg_age = 0
if midle_age > 0:
    midle_age *= 990
if other_age > 0:
    other_age *= 1390
if all_ticket > 3:
    print("Итого к оплате:", (youg_age + midle_age + other_age) - ((youg_age + midle_age + other_age)*10/100))
else:
    print("Итого к оплате:", youg_age + midle_age + other_age)