# class Square:
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#     def __str__(self):
#         return f'Square: {self.x}, {self.y}, {self.width}, {self.height}.'
# my_square = Square(5,10,50,100)
# print(my_square)

# class Rectangle:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def get_area(self):
#         return self.a * self.b
# rect_1 = Rectangle(3,5)
# print(rect_1.get_area())

# class Client:
#     def __init__(self, name, s_name, city, balance):
#         self.name = name
#         self.s_name = s_name
#         self.city = city
#         self.balance = balance
#     def get_client(self):
#         return f'{self.name} {self.s_name}. {self.city}. Баланс: {self.balance}.'
# user_1 = Client("Иван", "Петров", "Москва", 50)
# print(user_1.get_client())

class Client:
    def __init__(self, name, s_name, city, balance):
        self.name = name
        self.s_name = s_name
        self.city = city
        self.balance = balance
    def __str__(self):
        return f'{self.name} {self.s_name}. {self.city}. Баланс: {self.balance}.'
    def get_guest(self):
        return f'"{self.name} {self.s_name}. г.{self.city}."'

user_1 = Client("Иван", "Петров", "Москва", 50)

guest_1 = Client('Дмитрий', 'Селезнев', 'Череповец', 150)
guest_2 = Client('Ольга', 'Васильевна', 'Вологда', 150)
guest_3 = Client('Никита', 'Махалов', 'Тверь', 150)

list_guest = [guest_1, guest_2, guest_3]
for guest in list_guest:
    print(guest.get_guest())