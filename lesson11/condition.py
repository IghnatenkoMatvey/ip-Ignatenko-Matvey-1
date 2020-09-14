# Создаём рекурсивную блокировку
mutex = threading.RLock()

# Создаём переменную состояния и связываем с блокировкой
cond = threading.Condition(mutex)

#