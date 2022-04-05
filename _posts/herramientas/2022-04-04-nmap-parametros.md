---
layout: post
title: Nmap ,parámetros y funcionamiento básico
date: 2022-04-04
modified: 2022-04-04
description: explicación de los parámetros de nmap, funcionamiento y combinaciones con otros parámetros. 
tag:
 - pentesting
 - linux
 - herramientas
 - nmap
---
 
 **Actualmente no están todos los parámetros, solo los que he usado. (Nota: agregar imágenes)**

### Detección del sistema operativo

**-O** sirve para encontrar el sistema operativo por ejemplo si es un windows, linux o un mac.

***
### Detección de servicios y versiones

**-sV** brinda información los servicios y versión de los puertos abiertos.

***
### Especificación de destino

**-n** sirve para que no aplique resolución DNS (nota: esto puede aligerar en gran manera un escaneo).

**-R** siempre resolver DNS, el el contrario al parámetro `-n` (nota: este parámetro puede volver muy lento un escaneo).

***
### Descubrimiento de host 

**-Pn**  esta opción omite por completo la etapa de detección de hosts. Nmap de manera predeterminada determina las maquinas activas, hace detección de versiones y de sistemas operativos. con este parámetro desactivamos esto y hacemos que solo se centre en la ip especificada. 

***

### Técnicas de escaneo de puertos

**-sS**  escaneo TCP SYN. Indicamos que no queremos formar una conexión para descubrimiento de puertos abiertos, solo queremos que envié los paquetes sin entablar la conexión TCP esto por lo general aligera un escaneo. 

**-sT** escaneo de conexión TCP. Este parámetro es usado cuando el escaneo SYN (`-sS`) no es opción, esto ocurre cuando un usuario no tiene privilegios de paquetes sin procesar, con este parámetro decimos que forme la conexión para obtener la información de los puertos. Este tipo de escaneo es algo deficiente ya que tiene que formar una conexión y enviar mas paquetes para obtener la misma información que obtendría el SYN.

***

### Especificación del puerto y orden de escaneo

**-p** escanear puertos, si no agregamos `-p` por defecto solo buscara en los 1000 mas comunes pero podemos escanear puertos específicos si queremos (ejemplo: `-p 22,44,80`), si nos interesa escanear todo el rango de puertos también lo podemos hacer  (ejemplo: `-p-`) esto escaneara los 65635 puertos.

**-F** escaneo rápido, este parámetro reduce el numero de puertos que nmap escanea pasando de 1000 mas comunes a solo 100 mas comunes. 

**-r** no hacer un escaneo de puertos aleatorio. Nmap al realizar un escaneo no tiene un orden por defecto, con este parámetro especiamos que haga el escaneo en orden de puertos empezando por los menores y terminado con los mayores. 

***
###  Control de tiempo

**--min-rate** sirve para controlar directamente la velocidad de un escaneo emitiendo un numero mínimo de paquetes que queremos enviar (ejemplo: --min-rate 300).

**--max-rate**  sirve para controlar directamente la velocidad de un escaneo emitiendo un numero máximo de paquetes, normalmente usado para hacer un escaneo mas silencioso (ejemplo: --max-rate 100).

**-T** establecer una plantilla de tiempo, con esto definimos si queremos un escaneo lento o uno rápido. Hay que tener en cuanta que entre mas rápido mas ruido vamos hacer, este parámetro cumple la misma función que los parámetros `--max-rate, --min-rate` pero de manera mas simplifica puede ir del nivel 0 asta el nivel 5 (ejemplo: `-T0, -T1, -T2, -T3, -T4, -T5`).

***
### Scripts de Nmap

**-sC** scripts básicos de reconocimiento. es el equivalente a ``--script=default``(nota: algunos de los scripts lanzados suelen generar mucho ruido ).

***

###  Formatos de guardado 

**-v** Aplicación de verbose, este parámetro es para obtener mas información mientras el escaneo se realiza y lo puedes poner varias veces para obtener algo mas detallado obteniendo algo así (**-vvv**).

**-oN** formato de exportación para guardar información del escaneo.

**-oX** formato *XML* de exportación para guardar información del escaneo.

**-oG** formato *grepable* de exportación para guardar información del escaneo.

***
### Sin clasificación

**-A** nos brinda información del sistema operativo y sus servicios activos (nota: suele ser un parámetro muy ruidoso).

**--open** es un filtro para que solo nos muestre como resultado los puertos abiertos. 