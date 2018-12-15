Algoritmo AppMagic
	Definir codigo,nit,cont Como Entero
	Definir salario,nombre,apellido,salt,producto Como Caracter
	Definir precio Como Real
	Repetir
		Escribir '*|----------------|*'
		Escribir '*|    AppMagic    |*'
		Escribir '*|----------------|*'
		Escribir '_______OPCIONES_______'
		Escribir '1 Informacion'
		Escribir '2 Compra_Venta'
		Escribir '3 Marcas de telefono'
		Escribir '4 Ubicacoin'
		Escribir '5 Salir'
		Leer op
		Segun op  Hacer
			1:
				Escribir '¡¡¡¡¡INFORMACION!!!!!'
				Escribir 'App Magic. Somos una empresa dedicada al funcionamiento, mantenimiento y actuliazcion de tecologia.'
				Escribir 'Te ofrece las mejores marcas de Celulares a un precio increible!...'
			2:
				Repetir
					Escribir '########PRODUCTOS_EN_VENTA##########'
					Escribir '1. Samsung s9:               Q.9,000.00'
					Escribir '2. Iphone X:                Q.11,300.00'
					Escribir '3. Huawei Y9(2019):          Q.7,500.00'
					Escribir '4. Iphone XS:               Q.12,000.00'
					Escribir '5. Samsung A8:               Q.8,000.00'
					Escribir '6. Samsung J8:               Q.4,000.00'
					Escribir '-----LLENE LOS REQUISITOS-----'
					Escribir 'Nombre del Cliente: '
					Leer nombre
					Escribir 'Apellido del Cliente: '
					Leer apellido
					Escribir 'Direccion: '
					Leer direccion
					Escribir 'Codigo del Producto: '
					Leer codigo
					Escribir 'Nombre del producto: '
					Leer producto
					Escribir 'Precio del producto: '
					Leer precio
					Escribir 'Marca del producto'
					Leer marca
					Escribir 'Nit del Cliente: '
					Leer nit
					cont <- cont+1
					Escribir '########## FACTURA ##########'
					Escribir '****************no.',cont
					Escribir '...',nombre
					Escribir '...',apellido
					Escribir '...',direccion
					Escribir '...',codigo
					Escribir '...',producto
					Escribir '...',precio
					Escribir '... Q.',precio,'.00'
					Escribir '...'+marca
					Escribir '...',nit
					Escribir '#############################'
					Escribir 'DESEA CONTINUAR?... SI o NO: '
					Escribir '#############################'
					Leer salt
				Hasta Que salt='no'
			3:
				Escribir '1 Samsung'
				Escribir '2 Iphone'
				Escribir '3 Xiaomi'
				Escribir '4 Huawei'
				Escribir '5 Lenovo'
			4:
				Escribir 'Calzada Roosevelt 22-43, Ciudad de Guatemala 01011'
			5:
				Escribir 'Enter para finalizar'
				Esperar Tecla
			De Otro Modo:
				Escribir 'No te ama'
		FinSegun
	Hasta Que op=5
FinAlgoritmo

