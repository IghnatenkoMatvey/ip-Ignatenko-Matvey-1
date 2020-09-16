from  socket import*
import time
#
# s = socket(AF_INET, SOCK_STREAM)#создает сокет TCP
# s.bind(('', 8889))
# s.listen(5)
#
#
# while True:
#     client, addr = s.accept()
#     print("Получен запрос на соединение %s" % str(addr))
#     timestr = time.ctime(time.time()) + "\n"
#     client.send(timestr.encode('ascii'))
#     client.close()

#
host = 'localhost'
port = 9090
#настройки хоста и порта
clients = []

# создаем сокет
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port))
quit = False
print("[ Server Started ]")
# создаем сокет

while not quit:
    try:
        # принимаем данные с клиентов: данныеБадрес клиента
        data, addr = s.recvfrom(1024)
        # есл клиент "новый", добавляем его в наш список
        if addr not in clients:
            clients.append(addr)
        # текущее время
        itsatime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
        print("[" + addr[0] + "]=[" + str(addr[1]) + "]=[" + itsatime + "]/", end="")
        print(data.decode("utf-8"))
        for client in clients:
            if addr != client:
                s.sendto(data, client)
    except Exception as ex:
        print(ex)
        print("\n[ Server Stopped ]")
        quit = True