# # word = 'kyrGyzStan'
# #
# # print(word.upper())
# #
# # #KYRGYZSTAN
# #
# #
# # word = 'kyrGyzStan'
# #
# # print(word.lower())
# # #kyrgyzstan
# #
# # word = 'kyrGyzStan'
# #
# # print(word.capitalize())
# # #Kyrgyzstan
# #
# #
# # numbers1 = (5, 6, 7, 3, 2)
# # numbers2 = (7, 2, 4, 9, 3)
# # n1 = set(numbers1)
# # n2 = set(numbers2)
# # union_set = n1.intersection(n2)
# #
# # print(union_set)
# # #{3,2,7}
# #
# #
# # numbers1 = (5, 6, 7, 3, 2)
# # numbers2 = (7, 2, 4, 9, 3)
# # n1 = set(numbers1)
# # n2 = set(numbers2)
# # union_set = n1.intersection(n2)
# #
# # print(len(union_set))
# # #3
# #
# #
# #
# #
# #
# #
# # person = {'name': 'Aidanek', 'age': 33, 'department': 'IT'}
# # word = input('name: ').lower()
# #
# # if word in person:
# #     print(person[word])
# # else:
# #     print('jok')
# #     # kl.clova(name)
# #     #aidanek
# #
# #     cars = {'audi': 200, 'tesla': 500, 'bmw': 100, 'bugati': 150, 'tesla': 500}
# #     word = input('name: ', ).lower()
# #
# #     if word in cars:
# #         print(cars[word] // 2)
# #
# #     else:
# #         print('error')
# #
# #     # name: tesla
# #     #  {'audi':200, 'tesla':250, 'bmw':100, 'bugati':150, 'tesla':250}
# #
# #     # name: audi
# #     # {'audi':100, 'tesla':500, 'bmw':100, 'bugati':150, 'tesla':500}
# #
# #     # name: mers
# #     # Jok
# #
# #
# #
# #     numbers_one = [4, 9, -3]
# #     numbers_two = [10, 0, 3]
# #     work = numbers_one + numbers_two
# #
# #     work.sort(reverse=True)
# #     print(work)
# #     # [10, 9, 4, 3, 0, -3]
# #
# #
# #
# #
# #     names_one = {'Aigul', 'Asan', 'Ali'}
# #     names_two = {'Aidana', 'Mirbek', 'Ali'}
# #     work = names_two.difference(names_one)
# #
# #     print(work)
# #
# #     # {'Aidana', 'Mirbek'}
# #
# #
# #
# #
# #
# #
# #
# #     numbers = int(input("number: "))
# #
# #     for n in range(1, 11):
# #         print(f'{numbers} *{n}= {numbers * n}')
# #
# #
# #         # 2*1=2
# #         #2*2=4
# #         И.Т.Д
# #
# #
# #
# #         while True:
# #             number_one = int(input('1 санды жаз: '))
# #             number_two = int(input('2 санды жаз: '))
# #             znak = input("(+, -, *, /, Q): ")
# #
# #             if znak == '+':
# #                 print(number_one + number_two)
# #             elif znak == '-':
# #                 print(number_one - number_two)
# #             elif znak == '*':
# #                 print(number_one * number_two)
# #             elif znak == '/':
# #                 print(number_one / number_two)
# #             elif znak == 'Q':
# #                 break
# #             else:
# #                 print('Error')
# #
# # #1 санды жаз: 34
# # #2 санды жаз: 45
# # #(+, -, *, /, Q):
# # #Error
# # # санды жаз: 23
# # # санды жаз: Q   #kod toktodu
# #
# # metod1
# # num = int(input('number: '))
# #
# # while num != -1:
# #     print(num)
# #     num -= 1
# # else:
# #     print('The end')
# #
# #     metod2
# #
# #     num = int(input('number: '))  # 10
# #
# #     for i in range(num + 1):  # i = 2
# #         print(num - i)
# #     #number: 10
# # #10
# # #9
# # #8
# # #7
# # #6
# # ##4
# # #3
# # #2
# # #1
# # #0
# # #The end
# # #Process finished with exit code 0
# #
# #
# #
# #
# #
# # num = int(input('number: '))
# # n = 0
# # for i in range(1,num +1):
# #     n += i
# # print(n)
# #
# # # 15
# # # 1 2 3 4 5
# #
# # #2
# # #3
# # #1 2
# #
# #
# #
# #
# #
# # def sum_numbers(num):
# #     if num[0] < 0:
# #         return '0'
# #     elif min(num) >= 0:
# #         return 'ters san jok'
# #     result = 1
# #
# #     for i in num:
# #         if i <= -1:
# #             break
# #
# #         result *= i
# #
# #     return result
# # print(sum_numbers([4,5,6,3,-5,8,9,0]))
#
# def unique_elements(num):
#     w = set(num)
#
#     return w
#
# print(unique_elements([2,2,4,5,6,6,7,8,8]))
#
#
#
#
#
#
#
#
#
#
#
#
#
# total_money = [5000]
# class BankAccount:
#     def __init__(self,name,number):
#         self.name = name
#         self.number = number
#
#     def create(self, number, money):
#         if number == self.number:
#             total_money.append(money)
#             return sum(total_money)
#         else:
#             return f'number is undefind'
#
#     def delete(self,number,money):
#         if number == self.number:
#
#             return sum(total_money) - money
#         else:
#
#            return f'number is undefind'
#
#
#     def update (self,name,number):
#
#           return  self.number = numder
#
#
#
# user1 = BankAccount('Ali', 8950 )
# print(user1.delete(8950,500))
# #print(user1.info(8950))
# #4500
#
# print(user1.update('Ali', 6709))
# #print(user1.info(8950))
#
#
#
#
#
# class ToDoList:
#     def init(self):
#         self.tasks = {}
#
#     def add_task(self, task_id, task_description):
#         self.tasks[task_id] = task_description
#         return ''
#
#     def view_tasks(self):
#         for task_id, task_description in self.tasks.items():
#             print(f'{task_id} - {task_description}')
#
#     def update_task(self, task_id, new_task_description):
#         if task_id in self.tasks:
#             self.tasks[task_id] = new_task_description
#         else:
#             print('error')
#
#     def delete_task(self, task_id):
#         if task_id in self.tasks:
#             del self.tasks[task_id]
#         else:
#             print('error')
#
# todo_list = ToDoList()
#
# todo_list.add_task("1", "python дз")
# todo_list.add_task("2", "ООП ДЗ")
#
# todo_list.view_tasks()
# todo_list.update_task("1", "English 10 word")
# todo_list.view_tasks()
# todo_list.delete_task("2")
# todo_list.view_tasks()