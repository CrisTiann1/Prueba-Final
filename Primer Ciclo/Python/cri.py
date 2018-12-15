#!/usr/bin/env python
# -*- coding: utf-8 -*-
import webbrowser
import os
import time
def menu():
	os.system("cls")
	def INFO():
		print"""
		 ---------------
		| #############	|
		|    AppMagic   |
		| ############# |
		 ---------------

	AppMagic es una aplicacion de registro de compra y venta
	para encontrar el celular que mas necesite para su bien comun.
		"""
		exit = input("Si quieres salir, selecciona '1' de lo contrario, selecciona '0': ")
		if exit == 1:
			menu()
		elif exit == 0:
			INFO()
		else:
			menu()
	def compra_venta():
		venta = {"Samsung s9: ":10000, "Samsung A8: ":6500, "Samsung J8: ":3200, "iPhone X: ":11300, "iPhone XS: ":12000, "Huawei Y9(2019): ":7300}
		print"""
		°°°°°°°°°°°°°°°°°°°°°°°°°°
		----------------PRODUCTOS EN VENTA------------------
		°°°°°°°°°°°°°°°°°°°°°°°°°°
		"""
		cont = 0
		for y in venta:
			cont = cont + 1
			print str(cont) + "." + y + "Q." + str(venta[y]) + ".00"
		
		op = input("Que articulo desea obtener: ")
		if op == 1:
			codigo = int(input("Ingrese codigo de producto: "))
			nombre = raw_input("Ingrese nombre del comprador: ")
			apellido = raw_input("Ingrese apellido del comprador: ")
			direccion = raw_input("Ingrese direccion del comprador: ")
			nit = input("Ingrese Nit de Cliente: ")
			total = input("Ingrese total de compra: ")
			con = 0
			con = con + 1
			print"""
			--------------
			   FACTURA
			--------------
			"""
			print con
			print "Samsung s9  'Codigo del producto':  " + str(codigo)
			print "Nombre_Comprador:  " + nombre
			print "Apellido_Comprador:  " + apellido
			print "Direccion_Comprador:  " + direccion
			print "Abono de impuesto:  " + str(nit)
			print "TOTAL:  " + str(total) + ".00"
		elif op == 2:
			codigo = int(input("Ingrese codigo de producto: "))
			nombre = raw_input("Ingrese nombre del comprador: ")
			apellido = raw_input("Ingrese apellido del comprador: ")
			direccion = raw_input("Ingrese direccion del comprador: ")
			nit = input("Ingrese Nit de Cliente: ")
			total = input("Ingrese total de compra: ")
			con = 0
			con = con + 1
			print"""
			--------------
			   FACTURA
			--------------
			"""
			print con
			print "Samsung A8  'Codigo del producto':  " + str(codigo)
			print "Nombre_Comprador:  " + nombre
			print "Apellido_Comprador:  " + apellido
			print "Direccion_Comprador:  " + direccion
			print "Abono de impuesto:  " + str(nit)
			print "TOTAL:  " + str(total) + ".00"
		elif op == 3:
			codigo = int(input("Ingrese codigo de producto: "))
			nombre = raw_input("Ingrese nombre del comprador: ")
			apellido = raw_input("Ingrese apellido del comprador: ")
			direccion = raw_input("Ingrese direccion del comprador: ")
			nit = input("Ingrese Nit de Cliente: ")
			total = input("Ingrese total de compra: ")
			con = 0
			con = con + 1
			print"""
			--------------
			   FACTURA
			--------------
			"""
			print con
			print "Samsung J8  'Codigo del producto':  " + str(codigo)
			print "Nombre_Comprador:  " + nombre
			print "Apellido_Comprador:  " + apellido
			print "Direccion_Comprador:  " + direccion
			print "Abono de impuesto:  " + str(nit)
			print "TOTAL:  " + str(total) + ".00"
		elif op == 4:
			codigo = int(input("Ingrese codigo de producto: "))
			nombre = raw_input("Ingrese nombre del comprador: ")
			apellido = raw_input("Ingrese apellido del comprador: ")
			direccion = raw_input("Ingrese direccion del comprador: ")
			nit = input("Ingrese Nit de Cliente: ")
			total = input("Ingrese total de compra: ")
			con = 0
			con = con + 1
			print"""
			--------------
			   FACTURA
			--------------
			"""
			print con
			print "iPhone X  'Codigo del producto':  " + str(codigo)
			print "Nombre_Comprador:  " + nombre
			print "Apellido_Comprador:  " + apellido
			print "Direccion_Comprador:  " + direccion
			print "Abono de impuesto:  " + str(nit)
			print "TOTAL:  " + str(total) + ".00"
		elif op == 5:
			codigo = int(input("Ingrese codigo de producto: "))
			nombre = raw_input("Ingrese nombre del comprador: ")
			apellido = raw_input("Ingrese apellido del comprador: ")
			direccion = raw_input("Ingrese direccion del comprador: ")
			nit = input("Ingrese Nit de Cliente: ")
			total = input("Ingrese total de compra: ")
			con = 0
			con = con + 1
			print"""
			--------------
			   FACTURA
			--------------
			"""
			print con
			print "iPhone XS  'Codigo del producto':  " + str(codigo)
			print "Nombre_Comprador:  " + nombre
			print "Apellido_Comprador:  " + apellido
			print "Direccion_Comprador:  " + direccion
			print "Abono de impuesto:  " + str(nit)
			print "TOTAL:  " + str(total) + ".00"
		elif op == 6:
			codigo = int(input("Ingrese codigo de producto: "))
			nombre = raw_input("Ingrese nombre del comprador: ")
			apellido = raw_input("Ingrese apellido del comprador: ")
			direccion = raw_input("Ingrese direccion del comprador: ")
			nit = input("Ingrese Nit de Cliente: ")
			total = input("Ingrese total de compra: ")
			con = 0
			con = con + 1
			print"""
			--------------
			   FACTURA
			--------------
			"""
			print con
			print "Huawei Y9  'Codigo del producto':  " + str(codigo)
			print "Nombre_Comprador:  " + nombre
			print "Apellido_Comprador:  " + apellido
			print "Direccion_Comprador:  " + direccion
			print "Abono de impuesto:  " + str(nit)
			print "TOTAL:  " + str(total) + ".00"
		else:
			"ERROR"
		exit = input("Si quieres salir, selecciona '1' de lo contrario, selecciona '0': ")
		if exit == 1:
			menu()
		elif exit == 0:
			compra_venta()
		else:
			menu()
	def Marcas():
		print"	___MARCAS DE TELEFONOS___"
		marcas = ["Samsung", "iPhone", "huawei"]
		print "Marcas registradas: "
		for x in marcas:
			print x
		exit = input("Si quieres salir, selecciona '1' de lo contrario, selecciona '0': ")
		if exit == 1:
			menu()
		elif exit == 0:
			Marcas()
		else:
			menu()
	def Ubicacion():
		mostrar = input("mostrar ubicacion 1=si / 0=no: ")
		if mostrar == 1:
			webbrowser.open("https://www.google.com/maps/place/Centro+Comercial+Tikal+Futura/@14.6234259,-90.555622,17z/data=!3m1!4b1!4m5!3m4!1s0x8589a1a550ffffff:0x56a518886fdb2fe3!8m2!3d14.6234259!4d-90.5534333")
		elif mostrar == 0:
			Ubicacion()
		else:
			print "INCORRECTO"
	def salir():
		print"	____HASTA LUEGO____"
	os.system("cls")
	print """
	############################
	---------BIENVENIDO---------
	############################
	"""
	print"""
	#############################
	           AppMagic
	#############################

	__OPCIONES__:
		1. Informacion
		2. Compra y venta de Telefonos
		3. Marcas de Telefonos
		4. Ubicaciones
		5. SALIR
	"""
	a = input("Ingrese Numero de Opcion: ")
	if a == 1:
		INFO()
	elif a == 2:
		compra_venta()
	elif a == 3:
		Marcas()
	elif a == 4:
		Ubicacion()
	elif a == 5:
		salir()
	else:
		print"""
		######################
		...OPCION NO VALIDA...
		######################

		___INTENTA DE NUEVO___
		"""
menu()