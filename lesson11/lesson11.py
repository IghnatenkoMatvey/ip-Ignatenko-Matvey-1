# import threading
# import time
# def clock(interval):
#     while True:
#         print("Thread #{}, Текущее время: {}".format(threading.get_ident(),time.ctime()))
#         time.sleep(interval)
#
# if __name__ == '__main__':
#     t = threading.Thread(target=clock,args=(5,))
#     # t.daeman = True
#     t.start()
#
#
# import threading
# import time
#
# def clock(interval):
#     while True:
#         print("Thread #{}, Текущее время: {}".format(threading.get_ident(),time.ctime()))
#         time.sleep(interval)
#
# if __name__ == 'main':
#     threads = (threading.Thread(target=clock,args=(5,))
#                for _ in range(10))
#     for t in threads:
#         t.start()


import threading

protected_resource = 0
unprotected_resource = 0

NUM = 500000
mutex = threading.Lock()

def safe_plus():
    global protected_resource
    for i in range(NUM):
        mutex.acquire()
        protected_resource += 1
        mutex.release()

def safe_minus():
    global protected_resource
    for i in range(NUM):
        mutex.acquire()
        protected_resource -= 1
        mutex.release()

def risky_plus():

    global unprotected_resource
    for i in range(NUM):
        unprotected_resource += 1


def risky_minus():
    global unprotected_resource
    for i in range(NUM):
        unprotected_resource -= 1

if __name__ == '__main__':
    thread1 = threading.Thread(target = safe_plus)
    thread2 = threading.Thread(target = safe_minus)
    thread3 = threading.Thread(target = risky_plus)
    thread4 = threading.Thread(target = risky_minus)
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    print("Результат при работе с блокировкой %s" % protected_resource)
    print("Результат без блокировки %s" % unprotected_resource)


from threading import Semaphore

s = Semaphore(5)
# Если не передавать в семафор параметр
#семафор будет инициализирован 1
#(и таким образом станет обычной блокировкой)

s.acquire()# уменьшает счетчик на единицу -1
# ... доступ к общему ресурсу
s.release()# увеличивает счетчик на единицу +1























































































