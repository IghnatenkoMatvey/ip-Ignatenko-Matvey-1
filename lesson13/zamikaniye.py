def foo():
    x = 13
    array = ['lol','kek']
    def helloman():
        print('Привет,Мистер{}'.format(x))
        print('Вот твой список клиентов: {}'.format(array))
    return helloman

bar = foo()
bar()
# Посмотрим какие есть атрибуты у хелломэн
print(dir(bar))
# Если мы посмотрим, то увидим, что в замыкании есть два объекта
print(bar.__closure__)
# Выведем их
for attr in bar.__closure__:
    print(attr.cell_contents)
# Зададим ссылку .array2 ссылается на тот же объект в памяти?
array2 = bar.__closure__[0].cell_contents
# Проверим добавим ещё один элемент в массив и выполним функцию ещё раз
array2.append('cheburek')
bar()














































































