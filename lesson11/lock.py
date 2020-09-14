from threading import Lock

lock = Lock()
lock.acquire()
# ... код внутри блокировки
lock.release()