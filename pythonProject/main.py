# # # Напишите функцию `common_elements`, которая принимает два списка и возвращает новый список,
# # # содержащий общие элементы из обоих списков.
# #
# # # Пример использования:
# # # common_elements([1, 2, 3], [3, 4, 5])
# # # Ожидаемый результат: [3]
# #
# # def common_elements(num1,num2):
# #     work = set(num1).intersection(set(num2))
# #     return work
# # print(common_elements([1,2,3],[3,4,5]))
#
#
#
# # Напишите функцию `find_largest`, которая принимает список чисел и возвращает наибольшее число из списка.
#
# # Пример использования:
# # find_largest([3, 8, 1, 6, 4, 2])
# # Ожидаемый результат: 8
#
# # def find_largest(num):
# #     work = sorted(num)
# #     return work[-1]
# # print(find_largest([3, 8, 1, 6, 4, 2]))
#
#
#
# # Пример использования:
# # is_palindrome("radar");
# # Ожидаемый результат: True# Напишитз функцию `is_palindrome`, которая принимает строку и возвращает True, если она является палиндромом, и False в противном случ
#
# # def is_palindrome (soz):
# #     if soz == soz[::-1]:
# #         return 'true'
# #     else:
# #         return 'false'
# # work = input('soz jaz: ')
#
# # print(is_palindrome(work))a
#
# class Product:
#
#     def __init__(self):
#         self.products={}
#
#     def  create(self, name, description, price,kilo, category, date):
#         self.name = name
#         self.description = description
#         self.price = price
#         self.kilo= kilo
#         self.category = category
#         self.date = date
#
#     def read(self):
#
#         return f"{self.name} ,{self.description}, {self.price} *{self.kilo},{self.category}, {self.date}"
#
#
#
#     def update(self, name, new_description):
#         if name in self.products:
#             self.products[name] = new_description
#         else:
#             print('error')
#
#     def delete(self, price):
#         if price in self.products:
#             del self.products[price]
#         else:
#             print('error')
#     def sum_price(self):
#         return f'{self.price}* {self.kilo} = {self.price*self.kilo}'
#
# product1=Product()
#
# product1.create('apple ','gsjlgnf' ,140 ,6,'fruits','2024')
# product1.create('banana','fsvsv', 180,4,'fruits',2024)
# product1.update('apple','ygfbewib')
# product1.delete(140 )
#
# print(product1.create())


21.# Напишите функцию `remove_duplicates`, которая принимает список и возвращает новый список,
# в котором удалены все дубликаты.

# Пример использования:
# remove_duplicates([1, 2, 2, 3, 4, 4, 5])
# Ожидаемый результат: [1, 2, 3, 4, 5]

# def remove_duplicates(num):
#      w = set(num)
#      return w
#
# print(remove_duplicates([1,1,2,3,3,3,3,5,6,7,8,8]))







22. # Задача:
# Напишите функцию `is_prime`, которая принимает число и возвращает True, если оно нечетное, и False в противном случае.

# Пример использования:
# is_prime(7)
# Ожидаемый результат: True
def is_prime(num):
     if  num% 2!=0:
         return "true"
     else:
         return "false"
work=is_prime(7)
print(work)





23. # Задача:
# Напишите функцию `merge_lists`, которая принимает два отсортированных списка и возвращает новый отсортированный список,
# содержащий все элементы из обоих списков.

# Пример использования:
# merge_lists([1, 3, 5], [2, 4, 6])
# Ожидаемый результат: [1, 2, 3, 4, 5, 6]

# def merge_lists(num1,num2):
#     work = sorted(num2+num1)
#     return work
#
#
# print (merge_lists([1,3,5],[2,4,7,6]))
