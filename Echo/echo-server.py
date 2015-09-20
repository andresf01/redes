#!/usr/bin/python
# -*- coding: latin-1 -*-
# 
# Este es el programa server de un servicio de echo. Un servicio de echo (eco)
# como su nombre lo sugiere quiere decir que lo que recibe el servidor lo 
# regresa tal cual al cliente. Si el cliente envia un 'hola mundo' el servidor
# le regresara un 'hola mundo'.
#
# En este programa el cliente digitara una cadena se la enviara al servidor
# y este enviara la cadena de vuelta en pedazos de 16 bytes.
#
# Complete el programa en aquellas lineas que dice # tu codigo aqui
# Este servidor tiene como proposito escuchar a un cliente y enviarle de 
# regreso los datos por este enviados
#

import socket 
import sys
import argparse

host = ''
data_payload = 2048
backlog = 5 # valor que recibe la funcion socket.listen()

def echo_server(port): 
	# Cree un socket IPv4 y de tipo TCP
	#----------------
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print 'Socket created'	
	#----------------

	# Que el puerto de red del socket se pueda reutilizar
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_address = (host, port)
	print "Starting up echo server on %s port %s"%server_address
	# Asocie el socket s al server_address
	#----------------
	try:
		s.bind(server_address) # Esta funcion asocia un socket a un IP y un port
	except socket.error, msg:
		print 'Bind failed. Error code: ' + str(msg[0]) + ' message ' + msg[1]
		sys.exit()
	#----------------

	# Ahora escuche por clientes, use la variable backlog
	s.listen(backlog)
	print 'Socket listening'

	while True: # Esperando por conexiones de los clientes
		print "Esperando por mensajes de clientes"
		client, address = s.accept() # espera bloqueante por cliente
		# leer datos de una longitud maxima dada por la variable 
		# data_payload
		#--------------
		data = client.recv(data_payload)
		#--------------

		if data:
			print "Data: %s"%data
			# enviele los mismos datos al cliente
			#--------------
			client.send(data)
			#--------------
			print "send %s bytes back to %s"%(data,address)
	
	# cierre conexion con el cliente
	#---------------
	s.close()
	#---------------


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description = 'Socket Server Example')
	parser.add_argument('--port', action = 'store', dest = 'port', type = int, required = True)
	given_args = parser.parse_args()
	port = given_args.port
	echo_server(port)
