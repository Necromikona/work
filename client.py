#!/usr/bin/python3
from socket import *
import sys
import subprocess
import time
import toml

# Загружаем данные конфигурации из файла config.toml
config=toml.load("config.toml")
host = config['host']
port = config['port']
addr = (host,port)
timeout=config['timeout']
command=config['command']


while True:
	
	tcp_socket = socket(AF_INET, SOCK_STREAM)   # 	Открываем сокет с параметрами сети,
	tcp_socket.connect(addr) 				    # устанавливаем соединение с сервером.
	process = subprocess.Popen(command,stdout=subprocess.PIPE)             # 	Результ опроса WiFi соединений
	time.sleep(timeout)
	process.terminate()
	data=""
	data+=(str(process.stdout.read().decode('utf-8')))
	process.stdout.flush()
	print(data)		
	if not data : 								 
		data='No detected network'				# Выполняется проверка на наличие WiFi-соединений
	
	data = str.encode(data)                     
	tcp_socket.send(data)						# Выполняется отправка данных на сервер
	data = bytes.decode(data)
	data = tcp_socket.recv(1024)				# Получаем подтверждения от сервера о полученных данных
	data = bytes.decode(data)
	
	tcp_socket.close()
	time.sleep(timeout)
