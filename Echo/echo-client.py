#!/usr/bin/python
# -*- coding: latin-1 -*-
#
# Este es el programa cliente de un servicio de echo. Un servicio de echo (eco)
# como su nombre lo sugiere quiere decir que lo que recibe el servidor lo 
# regresa tal cual al cliente. Si el cliente envia un 'hola mundo' el servidor
# le regresara un 'hola mundo'.
#
# En este programa el cliente digitara una cadena se la enviara al servidor
# y este enviara la cadena de vuelta en pedazos de 16 bytes.
#
# Complete el programa en aquellas lineas que dice # tu codigo aqui
# 

import socket 
import sys
import argparse

host = 'localhost'

def echo_client(port): 
	# Cree un socket IPv4 y de tipo TCP
	#---------------
	try: # esta estructura permite capturar comportamientos anomalos
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except socket.error, msg: # si es del tipo socket.error
		print "Failed to create socket. Error code: " + str(msg[0]) + ", error message: " + msg[1] 
		sys.exit()
	#---------------

	server_address = (host, port)
	print "Connecting to %s port %s"%server_address

	# Conectese con el servidor
	#---------------
	s.connect(server_address)
	#---------------

	try:
		# El usuario digita la frase a enviar al servidor y lo guarda
		# en una variable llamada message
		#---------------
		message = raw_input('Send>> ')
		#---------------
		print "Sending %s"%message
		# Envie datos
		#---------------
		s.send(message)
		#---------------
		amount_received = 0
		amount_expected = len(message)
		while amount_received < amount_expected:
			# Reciba datos, no mas de 16 bytes
			#---------------
			data = s.recv(16)
			#---------------
			amount_received += len(data)
			print "Received: %s"%data
	except socket.errno, e:
		print "Socket error: %s"%str(e)
	except Exception, e:
		print "Other exception: %s"%str(e)
	finally:
		print "Closing connection to the server"
		s.close()
			

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description = 'Socket Server Example')
	parser.add_argument('--port', action = 'store', dest = 'port', type = int, required = True)
	given_args = parser.parse_args()
	port = given_args.port
	echo_client(port)
