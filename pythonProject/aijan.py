# # # word = 'AiJan KurmaNbekova'
# # #
# # # print(word.upper())
# # # #AIJAN KURMANBTKOVA
# # # cars = ['tesla','bmw','porshe','byd','audi']
# # # word = input('name: ')
# # #
# # # if word in cars:
# # #     total = cars.index(word)
# # #     print(total)
# # # else:
# # #     print('jok')
# # #
# # #
# # #
# # #
# # #     cars = ['tesla', 'bmw', 'porshe', 'byd', 'audi']
# # #     word = input('name: ').lower()
# # #
# # #     if word in cars:
# # #         total = cars.index(word)
# # #         print(total)
# # #     else:
# # #         print('jok')
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #         cars = {'audi': 200, 'tesla': 500, 'bmw': 100, 'bugati': 150, 'tesla': 500}
# # #         word = input('name: ', ).lower()
# # #
# # #         if word in cars:
# # #             print(cars[word] // 2 )
# # #
# # #         else:
# # #             print('error')
# # #
# # #         # name: tesla
# # #         #  {'audi':200, 'tesla':250, 'bmw':100, 'bugati':150, 'tesla':250}
# # #
# # #         # name: audi
# # #         # {'audi':100, 'tesla':500, 'bmw':100, 'bugati':150, 'tesla':500}
# # #
# # #         # name: mers
# # #         # Jok
# # #
# # #      metod1
# # #
# # # num = [5,3,7,9,0]
# # # summa =  0
# # # for n in num:
# # #     if n + summa :
# # #         summa = n+ summa
# # #
# # # print(summa)
# # # #24
# # #
# # # metod2
# # #
# # # num = [5,3,7,9,0]
# # # summa =  0
# # # for n in num:
# # #     summa += n
# # #
# # # print(summa)
# # # #24
# # #
# # #
# # #
# # # import random
# # #
# # #
# # # one = int(input('ot: '))
# # # two = int(input('do: '))
# # # print(random.randint(1,10))
# # #
# # #
# # # print(f'{one} mn {two} ortosyndagy sandy tap')
# # # while True:
# # #     o = int(input('san jaz: '))
# # #     print("tuura emes")
# # #
# # # else:
# # #     print('tuura')
# # #
# # # h/w
# # #     def check_numbers(x, z):
# # #         if x > z:
# # #             return x
# # #         elif z > x:
# # #             return z
# # #
# # #
# # #     print(check_numbers(11, 7))
# # #     # max is a
# # #
# # #     # print(check_numbers(10,7))
# # #     # max is 10
# # #     d
# # #
# # #
# # # def perimetr (a,b,c):
# # #     return a+b+c
# # # print(perimetr(5,6,5))
# # #
# # #
# # #
# # # def colors(*args):
# # #     return args[::-1]
# # #
# # #
# # # print(colors('orange','red','blue'))
# # #
# # #
# #  def colors(v):
# #    return v.upper()
# #
# #
# #  print(colors('blue',))
#
#
#
# def merge_lists(num1,num2):
#    f =num1+num2
#    x =sorted(f)
#    return x
#
#
# print (merge_lists([1,3,5],[2,4,6]))A
#
#
#
# # Ожидаемый результат: [1, 2, 3, 4, 5, 6]
#
#
#
#
# def merge_lists(num1,num2):
#    word = set(num1).intersection(set(num2))
#    return word
#
# print (merge_lists([1,3,5],[2,5,4,6]))
#
#
#
# # Ожидаемый результат: {5}
#
#
# def merge_lists(numbers):
#    f =[]
#    for i in range(len(numbers)):
#        f.append(numbers[i]*i)
#    return f
#
#
# print (merge_lists([1,2,3,4,5]))
#
#
#
# # Ожидаемый результат: [0,2,6,12,20]
#
#
#
#
#
#
#
#


def latter(lst):
    work = ['а','и','о','е','ё','у','ы','э','ю ','я']
    result = []
    for bukva in lst:
      if bukva.lower() in work:
       result.append(bukva.lower())

    return len(result)


print(latter('Мен Айжан Курманбекова'))#8


class Product:
    def __init__(self, title, description, price, category, date):
        self.title = title
        self.description = description
        self.price = price
        self.category = category
        self.date = date

    def get_info(self):
        return f"{self.title} ,{self.description}, {self.price} ,{self.category}, {self.date}"


product1 = Product('banana', 'dhbsjk', 150, 'fruits', "22.04.2024")

print(product1.get_info())

# 'T-shirt', 'dfgdgfdgds:', 4555, 'Clothes', 22-3-2024


class Product:
    def __init__(self, title, description, price, category, date):
        self.title = title
        self.description = description
        self.price = price
        self.category = category
        self.date = date

    def get_info(self):
        return f"{self.title} ,{self.description}, {self.price} ,{self.category}, {self.date}"


product1 = Product('banana', 'dhbsjk', 150, 'fruits', "22.04.2024")


class Laptop:
    def __init__(self, title, description, price, category, date):
        self.title = title
        self.description = description
        self.price = price
        self.category = category
        self.date = date

    def get_info(self):
        return f"{self.title} ,{self.description}, {self.price} ,{self.category}, {self.date}"


laptop1 = Laptop('sfggg', 'sagag', 234, 'laptop', '2024')

print(product1.get_info())
print(laptop1.get_info())

# 'T-shirt', 'dfgdgfdgds:', 4555, 'Clothes', 22-3-2024


class Employee:
    def __init__(self, name,salary):
        self.name = name
        self.salary = salary

    def get_info(self):
        return f'{self.name}{self.salary}'

    def sum_salary(self):
     pass


class Manager(Employee) :
    def __init__(self,name, salary, department):
        super().__init__(name,salary)
        self.department = departmenta

    def get_info(self):
       return (f'{self.name},{self.salary},{self.department}')



    def check(self):
        if self.department == 'it':
            return 'Cool'
        else:
            return 'no cool'

print()
class Intern(Employee) :
    def __init__(self,name, salary ,year):
        super().__init__(name,salary,)
        self.year = year

    def get_info(self):
        return f'{self.name},{self.salary},{self.year}'

    def sum_salary(self):
     return f'{self.salary*(self.year*12)}'

emloyee1 = Employee('Aman',30000)

intern1 =Intern('Aman',30000,4)

meneger1 = Manager('Aman',30000,'it')

print(meneger1.check())
print(intern1.sum_salary())

