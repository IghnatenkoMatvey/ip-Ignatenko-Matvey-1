# string = 'Hello'
# string_test = 'asasasasasasasasyy'
# print(string[1:3])
# print(string[:3])
# print(string[1:5:])
# print(string[:-1])
# print(string[6:1])
# a = 'start'
# b = 'stop'
# c = 'step'
# string[a:b:c] индексация начинается с 0
# .title(),.upper(),.lower(),.find() etc.
# print(string.find('ll'))
# # print(string_test.find('yy'), len(string_test))
# name = 'Eric'
# surname = 'Smith'
# print('Welcome ' + name + ' ' + surname + '!')
# print('Welcome {} {}!'.format(name,surname))
# print('Welcome {1} {0} !'.format(name, surname))
# print(f'Welcome {name} {surname} !')
# empty_list =[]
# list = [1,2,3,4,5,6,7,8,9]
#  print('My list: ', list)
#  print('My list: ', list * 300)
# list = [1,2,3,4,5,6,7,8,9]
# print(0 in list)#false
# print(7 in list)#true
# list = [1, [1, [3]]]
# print(list[1][1][0])# 3
# list.append(['1', 3.2])
# print(list)
# lst = [1,2,3]
# lst.append(1)# добавить в конец списка
# lst.pop()# удалить последний элемент
# lst.pop(2)
# print(lst)
# удалить элемент с индексом 4
# t = (2)
# print(t)
# t =(2, )
# print(t)
# t = 2,
# print(t)
# x = {}
# {ключ : значение}
# print(x)
# x['y'] = '1'
# print(x)
# x['y'] = {'1' : 1}
# print(x)


# # цикл по словарю
# for key, value in x.items():
#     print (key,value)
# for key in x.keys():
#     print(key)
# for value if x.values():
#     print(value)
# # удаляет элемент и возвращает его значение
# print(x.pop('c'))
# print(x)
#print(x.popitem()) # удаляет и возвращает произвольную пару (ключ, значение)

# a = set()
# print('a = ', a)
# b = set(['a','b','c','c','a','e'])
# print('b = ', b)
# c = set('hello')
# print('c = ', c)
# d = ['a','b','c','d']
# print('d = ', d)
# f = {} # а так получится словарь
# print('type({}) -->',type(f)) #<class 'dict'>
# #Операции со множествами
# print(len(e))
# print(''b' in b -->', 'b' in b)
# # s == t
# c1 = {'e','l','o','h'}
# print(c == c1)
# # s.issubset(t) s<= t
# print(c >={'h'})

a = set(['a','3','5'])
b = set(['a','3'])
print(a)
print(b.issubset(a))

# s.issubset -  подмнжество
# s.issuperset - надмножество
# s.union - объединение множеств
# s.intersection - сходство
# s.difference - различие
#s.symmetric_difference - либо в одном элементе есть либо в другом, но не в обоих множествах

myset = {1,2,3,5}
second_set = {1,2,7}
print(myset.intersection([1,2]))
print(myset.difference([1,2,7]))
print(second_set.difference(myset))
