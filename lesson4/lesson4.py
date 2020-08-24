 # for i in range(0,8,2): # range (1,2,3) 1 - начало 2 - конец 3 - шаг
#     print(i)
#abs(-2)  #  вывод абсолютной величины
# print(max([1,2,3,4,5])) # максимальный элемент последовательности, аналогично работает min() только в обратную сторону
# x = round(2.56,1) округление до н знаков
#x = summ([2.56,1,12]) суммирует все элементы последовательности
# x = type('') # возвращает тип объекта
# x = [1,2,4,5]
# for i, y in enumerate(x): # возвращает пару индекс и значение
# #     print(i,y)
# def summ(a,b):
#     c = a + b
#     return c
# x = 5
# y = 6
# s = summ(x,y)
# print(s)
# f = lambda x: x ** 2
# print(f(4))
# print((lambda x: x ** 2)(4))
# x = 5
# def outside():
#     y = 10
#     def inside():
#         z = 15
#         print('inside x:{},y:{},z{}'.format(x,y,z))
#     inside()
#     print('outside x: {},y: {},z: {})'.format(x,y,'z недоступна'))
# outside()
# print('inside x: {},y: {},z: {}'.format(x,'y недоступна', 'z недоступна'))
# x = 5
# def wrapper():
#     def test1():
#         x = 10
#         print('test1 x = ',x)
#     def test2():
#         print('test2 x = ', x)
#     def test3():
#         global x
#         print('test3 x = ',x)
#         x = 25
#     test1()
#     test2()
#     test3()
# wrapper()
# print('after wrapper x = ',x)

# def average(*args):
#     summ = 0
#     for arg in args:
#         summ += arg
#     return summ / len(args)
# print(average(1, 2, 3))

# def print_info(**kwargs):
#     print("Your name is %s %s. Your age is %s. And your adress is: %s"%
#     (kwargs['name'],kwargs['surname'],kwargs['age'],kwargs['adress']))
# print_info(name = 'Vasiliy', surname = 'Ivanov',age = '12',adress = 'st.Belana 22')

# def welcme(name="Inkognito"):
#     print("Hello,%s"%(name))
# print('Ivan','Ivanovich','Ivanov',sep='//',end='!!!')
# a = [1, 2, 4]
# b = [3, 4]
# c = [5, 6, 0]
#
# for i in zip(a,b,c):
#    print(i)
   # zip - итератор который генерирует серию множеств содержащую элементы из каждой итерации

# print(list(map(lambda x: x*x,[2,5,12,-2])))
# map - применяет функцию к каждому элементу последовательности, результат функции возвращает в виде итератора

# print(list(filter(lambda x: x > 5,[2,10,-10,8,2,0,14] )))
# print(list(filter(len,["",'not null','bla',"",'10'])))
# import os
# path = 'files/text.txt'
# path = os.path.join
# f = open(path, 'r', encoding='UTF-8')
# # считываем всю информациюиз файла в виде списка строк
# print(f.readlines())
# f.close()
# Baldddej
# path = os.path.join('files',;'text.txt')
# f = open(path,'r',encoding='UTF-8')
# wanted_symbol = "+"
# for line in f:
#     if wanted_symbol in line:
#         print(line)
#         break
#
# with open(path,'r', encoding='UTF-8') as f:
#     print(f.readlines())