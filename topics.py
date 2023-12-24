#Типы данных
# a = 12 #intiger
# b = 12,5 #float
# c = 'Dog' #string
# True or False #boolean

#Математические операторы
# a = 13 + 5 
# b = 13 - 5
# c = 13 * 5
# d = 13 / 5
# e = 13 % 5 #выводит толька остаток
# f = 13 // 5 #без остатка

#Форматирование строк
# print(f'Bla bla bla bla {a}')



#Условные операторы
# if a == 1:
#     print(True)
# elif a != 1:
#     print(False)
# else:
#     print(None)


#Списки и Кортежи
# List = [1, 2, 3, 'P1']
# Cortage = (1, 2, 3, 'P1')


#Циклы
# for i in range(1, 11):
#     print(i)

# while True:
#     print('Hello')

#List comperhension  
# nums = [1, 22, 333, 4444, 55555]
# func = [i + 1 for i in nums if i = 2]

#Dictionary and Sets
# jobs = {'Bob':'Taxi'}
# nums = set({1, 1, 1, 1 ,1, 2, 2, 2, 2})


#Функцы 
# def print_hello():
#     print('Hello')

# print_hello()

#Фенкцы 2
# x = lambda e: e

# print(x(9))
# def spam(*args):
#     for a in args:
#         print(a)

# spam(1, 2, 3, 4, 1, 2, 3, 4, 'Hello')

# math(6,3,9)

# def spam(**kwargs):
#     for k,v in kwargs.items():
#         print(k,v)

# spam(name='my1',age=23)


#Class
# class Cars:
#     def __init__(self, model, color, speed, year):
#         self.model = model
#         self.color = color
#         self.speed = speed
#         self.year = year

# mclaren = Cars('P1', 'Black', 365, 2023)

# print(mclaren.model)

#Class 2
# class MyClass:
#     def __init__(self, value):
#         self.value = value


#     @classmethod
#     def multiply(cls,value):
#         return value**2
    

# print(MyClass.multiply(5))

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height


#     @property
#     def area(self):
#         return self.width * self.height
    
# rectangle = Rectangle(4, 7)
# print(rectangle.area)

# rectangle.width = 7
# print(rectangle.area)
