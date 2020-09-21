def factorial(n):
    """ Вычисляет факториал числаю например: >>> factorial(6)
    720
    """
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial.__doc__.)