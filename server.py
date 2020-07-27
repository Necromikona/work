#!/usr/bin/python3
from socket import *
import toml 

# Загружаем данные конфигурации из файла config.toml
config=toml.load("config.toml")
port = config['port']
host = config['host']
addr = (host,port)
size=config['size']

tcp_socket = socket(AF_INET, SOCK_STREAM)  # Открываем сокет с параметрами сети
tcp_socket.bind(addr)					   # Cвязываеv адрес и порт с сокетом
tcp_socket.listen(5)					   # Устанавливаем количество клиентских соединений, которые будет обслуживать операционная система.

while True:
    conn, addr = tcp_socket.accept()       # Принимаем запрос
    data = conn.recv(size)				   # Получаем сообщение
    data = bytes.decode(data)
    
    if not data:
    	continue
    
    print(data)
    conn.send(b'Complete')				   # Отправляем подтверждение
    conn.close()
    
tcp_socket.close()
