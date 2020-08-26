# f = open('1.txt')
# ints = []
# try:
#     for line in f:
#         ints.append(int(line))
# except ValueError(# здесь может быть любая конкретная ошибка):
#     print('Thi is not a nuber.Exit')
# except Exception:
#     print('What is it?')
# else:
#     print('everything is ok')
# finally:
#     f.close()
#     print('I closed the file')
    # Именно в таком порядке: try, группа except, than else, and than finally.
# print('start')
# try:
#     val = int(input('input number: '))
#     tmp = 10 / val
#     print(tmp)
# except ValueError as ve:
#     print('ValueError! {0}'.format(ve))
# except ZeroDivisionError as zde:
#     print('ZeroDivisionError! {0}'.format(zde))
# except Exception as ex:
#     print('Error {0}'.format(ex))
# print('stop')


# try:
#     raise Exception('Some exception')
# except Exception as e:
#     print('Exception exception ' + str(e))
# import math
# print(math.sqrt(4))
# from math import sqrt
# from math import sqrt, sin, cos
# print(sin(0.2))



# import libs as my_lib
# print(my_lib.do_something())
# print(my_lib.more_than_one(6))


# import os
# print('os.name = ', os.name)
# print('os.getcwd() = ', os.getcwd())
#
# dir_path = os.path.join(os.getcwd(),'NewDir')
# try:
#     os.mkdir(dir_path)
# except FileExistsError:
#     print('Такая директория уже существует')


# import sys
# # Список аргументов запуска скрипта
# #первым аргументом является полный путь к файлу скрипта
# print('sys.argv = ',sys.argv)
# # Список путей для поиска модулей
# print('sys.path = ',sys.path)
# # Полный путь к интепретатору
# print('sys.executable = ',sys.executable)
# # Словарь имён загруженных модулей
# print('sys.modules = ',sys.modules)
# # Информация об операционной ситсеме
# print('sys.platform = ',sys.platform)
# while True:
#     key = input("press 'q' to Exit")
#     if key == "q":
#         sys.exit()
#         # Вызов данной функции мгновенно завершает работу модуля(скрипта)


# import sys
# import argparse
#
# def createParser():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('name',nargs = '?', default = 'world')
#     return parser
# if __name__ == '__main__':
#     parser = createParser()
#     namespace = parser.parse_args(sys.argv[1:])
#     print('Hello, {}!'.format(namespace.name))





















































































































































