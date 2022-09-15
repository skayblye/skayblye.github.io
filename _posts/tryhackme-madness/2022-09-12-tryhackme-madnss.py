Iniciamos la maquina con un scaneo de puertos de nmap.

	nmap -p- --min-rate 5000 -sS -vvv -n -Pn --open -oG ports 10.10.108.64

El cual no regresa que solo hay dos puertos activos, el 22 con el servicio ssh y el 80 corriendo un servidor con http.

	# Nmap 7.92 scan initiated Mon Sep 12 12:20:45 2022 as: nmap -p- --min-rate 5000 -sS -vvv -n -Pn --open -oG ports 10>
	# Ports scanned: TCP(65535;1-65535) UDP(0;) SCTP(0;) PROTOCOLS(0;)
	Host: 10.10.108.64 ()   Status: Up
	Host: 10.10.108.64 ()   Ports: 22/open/tcp//ssh///, 80/open/tcp//http///        Ignored State: closed (65533)
	# Nmap done at Mon Sep 12 12:21:00 2022 -- 1 IP address (1 host up) scanned in 15.33 seconds

Al solo tener dos puertos abiertos, entraremos directamente a ver el servidor htttp abierto. Al entrar nos encontramos con la página por defecto de apache2. 

imagen del servidor apache 

En este punto pensé en tirar de `wfuzz`, pero no encontré nada, así que fue una pérdida de tiempo. Pero si miramos la página más detenidamente. nos encontraremos con un pequeño pixel.

 imagen del pixel

Al no poder verlo, hay que descargarlo y ver cuál es el problema con la imagen. Haciendo uso de `wget` nos descargaremos la imagen.

	wget http://10.10.50.135/thm.jpg

una vez descargado vemos algo raro, Los números mágicos pertenecen a un archivo PNG, pero su extensión es JPG. Y si queremos abrir el archivo nos encontraremos con el mismo problema.

Así que hay que cambiar los números por su valor correspondiente. Haciendo una búsqueda en Google, vemos que su valor original debería ser `ff d8 ff e0 00 10 4a 46 49 46 00 01`asi que corregimos esto usando `hexedit`Nota: por alguna razon no viene instalado en parrot, pero lo podemos instalar. `sudo apt install hexedit`

inserte imagen del editor,
inserte imagen desbloqueada

En la imagen vemos una ruta nueva y si la ponemos en el navegador nos llevara a una página web.

inserte imagen de papagina web y del view source

Por lo que dice, me nos damos una idea de lo que hay que hacer, aunque hay que hacerlo de una manera algo especifica. Si solo escribimos la ruta 1,2,3, etc, nunca llegaremos a nada. hay que escribirlo como si fuera una variable.

	http://10.10.50.135/th1s_1s_h1dd3n/?secret=0

inserte imagen del url

Ahora que sabemos que hacer, podríamos escribir número por número hasta dar con el resultado, pero en este caso burpsuite puede ser una mejor opción.

Entraremos a burp e interceptaremos la primera petición. 

inserte imagen de proxy de burp
inserte imagen de sniper burp

Pero...antes de iniciar necesitamos un pequeño archivo que contenga los 100 números, para este problema, solo aremos un script de python.

	for i in range(0,100):
		print(i)

Ejecutaremos el script y se lo pasaremos a un archivo txt para que nos guarde los números generados.

	python3 numeros.py > numeros.txt

Y listo, ahora tenemos los 100 números. Podemos regresar a burp y emplear el taque sniper, solo hay que agregar la lista que acabamos que hacer.

inserte imagen de ataque 

Una vez finalizado, vemos que la única respuesta diferente fue el numero 73. 

El código que nos dio parece ser más una contraseña, al verificar 