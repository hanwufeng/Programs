"# -*- coding: utf-8 -*- "
'''
=================================================================================================
Descripción: Script para extraer configuraciones de switches, usando conexion SSH y Telnet.
Autor: Yo @brazzinioc. Autorizo su uso, modificación y distribución de este script.
Email: brazziniogosi@gmail.com
fecha: 04-03-2018
Version: 3.0
=================================================================================================
'''
#Módulos importados
#=========#
import  sys, paramiko, time, telnetlib

# Extracción de la Versión de Python instalado
version = int(sys.version_info[0]) 

# Comprobación de la versión de python, para ejecutar el script
if(version >= 3):

	#Funciones
	#=========#

	def extract_system_data():
		# Extracción de datos del sistema
		hora = time.strftime("%I-%M-%S") # Hora del sistema operativo
		fecha = time.strftime("%Y%d%m") # Fecha del sistema operativo
		output = str(fecha) + "_" + str(hora) #Concatenación de fecha y hora
		return output #retorno de fecha mas hora

	def extract_config_from_hostname_SSH(ip_address, username_ssh, password_ssh, command, ip_ftp, backupFileName):
		
		systemData = extract_system_data() #Obtención fecha y hora del Sistema
		nameFile = backupFileName + "-"  + ip_address + "-" + systemData #Elaboración de nombre de fichero para almacenar datos obtenido, con el comando.

		ssh = paramiko.SSHClient() #Creación de Objeto Cliente SSH
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #Política para agregar automáticamente el nombre de host y la nueva clave.
		ssh.connect(ip_address, username=username_ssh, password=password_ssh) #Conexión SSH, enviando usuario y password.
		print("Connection Success ") #Mensaje de Conexión exitosa.
		stdin, stdout, stderr = ssh.exec_command(command) #Ejecución de comando.
		time.sleep(3) #Tiempo de espera de 3 Segundos.
		stdin.write(ip_ftp + "\n") #Envío de IP del servidor FTP más enter.
		time.sleep(3) #Tiempo de espera de 3 segundos.
		stdin.write(nameFile + "\n") #Envío de nombre de backup más enter
		time.sleep(5) #Tiempo de espera de 3 Segundos.
		print("Session SSH closed.") #Mensaje
		ssh.close()#Cerramos sesión SSH.
		
		#Generación y guardado de Log
		logFile = open('log.txt', 'a') #Creación y apertura de archivo log
		logFile.write("Fecha: " + systemData + " NombreFichero: " + nameFile + "\n") #Insertamos fecha y nombre de backup en archivo log
		logFile.close() #Cerramos archivo log
		
		return print("Success.! :)") #Retornamos mensaje.






	def extract_config_from_hostname_Telnet(ip_address, username_telnet, password_telnet, ip_ftp, command, backupFileName):
		systemData = extract_system_data() #Obtención fecha y hora del Sistema
		nameFile = backupFileName + "-"  + ip_address + "-" + systemData # Elaboración de nombre de fichero de Backup.
		tn = telnetlib.Telnet(ip_address, 23) #Creación de Objeto Telnet
		tn.read_until(b"Username: ") #Lectura de la cadena encontrada luego de la conexión Telnet
		print("Pasando telnet username..") #Mensaje
		tn.write(username_telnet.encode('utf-8') + b"\r\n") #Envío de usuario más enter.

		tn.read_until(b"Password: ") #Lectura de la cadena encontrada luego del envío de usuario.
		print("Pasando password..") #Mensaje
		tn.write(password_telnet.encode('utf-8') + b"\r\n") #Envío de contraseña más enter.
		print("Autentication Success :D") #Mensaje

		print("Ejecutando comando: {}".format(command)) #Mensaje
		tn.write(command.encode('utf-8')  + b"\r\n") #Envío del comando más enter.
		time.sleep(5) #Tiempo de espera - 5 segundos.
		print("Ingresado Host FTP: {}".format(ip_ftp)) #Mensaje
		tn.write(ip_ftp.encode('utf-8')  + b"\r\n")# Envío del host del servidor FTP.
		time.sleep(5) #Tiempo de espera - 5 segundos
		print("Ingresado nombre de Backup: {}".format(nameFile)) #Mensaje
		tn.write(nameFile.encode('utf-8') + b"\r\n")# Envío de nombre de Backup
		time.sleep(2) #Tiempo de espera - 2 segundos

		print("Operación completada") #Mensaje

		print("Cerrando sesion.") #Mensaje
		tn.close() #Cerramos sesión Telnet.

		#Generación y guardado de Log
		logFile = open('log.txt', 'a') #Apertura de archivo log
		logFile.write("Fecha: " + systemData + " NombreFichero: " + nameFile + "\n") #Insertamos fecha y nombre de backup en archivo log
		logFile.close() #Cerramos archivo log



	#INVOCACIÓN DE LA FUNCIÓN "extract_config_from_hostname_SSH"
	#==========================================================#
	#Diccionario de Switches que usan SSH
	#Si se desea agregar o eliminar Switch verifique este diccionario.
	switches_ssh = [
	{"IP_ADD":"192.168.0.10" , "USER_SSH":"sshuser" , "PASS_SSH":"passssh" , "COMMAND":"copy running-config ftp:" , "FTP_HOST":"192.168.0.100", "FILENAME":"sw5toPiso" },
	{"IP_ADD":"192.168.0.11" , "USER_SSH":"sshuser" , "PASS_SSH":"passssh" , "COMMAND":"copy running-config ftp:" , "FTP_HOST":"192.168.0.100", "FILENAME":"sw6toPiso" },
	{"IP_ADD":"192.168.0.12" , "USER_SSH":"sshuser" , "PASS_SSH":"passssh" , "COMMAND":"copy running-config ftp:" , "FTP_HOST":"192.168.0.100", "FILENAME":"sw7moPiso" },
	{"IP_ADD":"192.168.0.13" , "USER_SSH":"sshuser" , "PASS_SSH":"passssh" , "COMMAND":"copy running-config ftp:" , "FTP_HOST":"192.168.0.100", "FILENAME":"sw8voPiso" },
	{"IP_ADD":"192.168.0.14" , "USER_SSH":"sshuser" , "PASS_SSH":"passssh" , "COMMAND":"copy running-config ftp:" , "FTP_HOST":"192.168.0.100", "FILENAME":"sw9noPiso" }]

	#Recorrido del diccionario de Switches que usan SSH.
	for sw in switches_ssh:
		extract_config_from_hostname_SSH(sw["IP_ADD"], sw["USER_SSH"], sw["PASS_SSH"], sw["COMMAND"], sw["FTP_HOST"], sw["FILENAME"])


	#INVOCACIÓN DE LA FUNCIÓN "extract_config_from_hostname_Telnet"
	#==========================================================#
	#Diccionario de Switches que usan Telnet
	#Si se desea agregar o eliminar Switch verifique este diccionario.
	switches_telnet = [
	{"IP_ADD":"192.168.0.2", "USER_TELNET":"username", "PASS_TELNET" : "Passw", "FTP_HOST":"192.168.0.100", "COMMAND":"copy running-config ftp:", "FILENAME":"Sw88toPiso"}
	]

	#Recorrido del diccionario de Switches que usan Telnet
	for sw in switches_telnet:
		extract_config_from_hostname_Telnet(sw["IP_ADD"], sw["USER_TELNET"], sw["PASS_TELNET"], sw["FTP_HOST"], sw["COMMAND"], sw["FILENAME"])


else:
	#Mensaje de instalación de Python v3.6
	url = 'https://www.python.org/downloads/'
	print("Por favor, instale Python v3.6 e intente nuevamente.")
	print("Descargue desde: {url}".format(url=url))
