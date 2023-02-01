all_ticket = int(input("Введите количество билетов"))
#Это была первая попытка решить задачу :)
# young_age = int(input("Сколько слушателей менее 18 лет?"))
# middle_age = int(input("Сколько слушателей от 18 до 25 лет?"))
# other_age = int(input("Сколько слушателей старше 25 лет?"))
# sale = 10
# if young_age > 0:
#     young_age = 0
# if middle_age > 0:
#     middle_age *= 990
# if other_age > 0:
#     other_age *= 1390
# if all_ticket > 3:
#     print("Итого к оплате:", (young_age + middle_age + other_age) - ((young_age + middle_age + other_age)*sale/100))
# else:
#     print("Итого к оплате:", young_age + middle_age + other_age)
#Итоговый код решения задачи
final_price = 0
for i in range(1, all_ticket + 1):
    any_ticket = int(input("Введите возраст слушателя"))
    if any_ticket < 18:
        final_price += 0
    elif 18 <= any_ticket < 25:
        final_price += 990
    else:
        final_price += 1390
if all_ticket > 3:
    final_price *= 0.9
print("Итого к оплате:", final_price)
