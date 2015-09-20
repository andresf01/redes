#/usr/bin/python
import socket
import sys
from thread import *

HOST = '' # Este servidor escuchara por todas las interfaces de red
PORT = 8888 # Un identificador de puerto cualquiera

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print 'Socket created'

try:
	s.bind((HOST, PORT)) # Esta funcion asocia un socket a un IP y un port
except socket.error, msg:
	print 'Bind failed. Error code: ' + str(msg[0]) + ' message ' + msg[1]
	sys.exit()

print 'Socket bind complete'

s.listen(10)
print 'Socket bind complete'

# Funcion para manejar las conexiones. Se crea un hilo por cada cliente que se conecta
def clientthread(conn):
    # Se envia un mensaje al cliente conectado
    conn.send('Welcome to the server. Type something and hit enter\n')
     
    # Ciclo infinito para que la funcion no termine y tampoco el hilo.
    while True:
         
        # Se reciben datos del cliente
        data = conn.recv(1024)
        reply = 'OK...' + data
        if not data: 
            break
     
        conn.sendall(reply)
     
    # Si termina el ciclo se cierra la conexion
    conn.close()

while 1:
    # Espera por una conexion, la funcion accept() bloquea la ejecucion hasta recibir una conexion
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])

    # La funcion start_new_thread() recibe la funcion que representa el hilo y la tupla de argumentos de la funcion del hilo
    start_new_thread(clientthread ,(conn,))
 
s.close()

