---
layout: post
title: Wfuzz ,parámetros y funcionamiento básico
date: 2022-04-05
modified: 2022-04-05
description: explicación de los parámetros de wfuzz, funcionamiento y combinaciones con otros parámetros. 
tag:
 - pentesting
 - linux
 - herramientas
---

##  ¿Qué es wfuzz?

Wfuzz es una herramienta de fuerza bruta web que cuenta con diferentes complementos de aplicaciones web como: parámetros, autenticación, formularios, directorios/archivos, cabeceras, etc. 

Wfuzz también cuenta con otras utilidades como lo es actuar de escáner de vulnerabilidades de aplicaciones web. Es completamente modular por que fácilmente puedes crear y instalar plugins.

Nota: Usamos la palabra `FUZZ`al final de la solicitud http para indicar donde aplicar fuerza bruta (Ejemplo `http://testphp.vulnweb.com/FUZZ`).

Actualmente no están todos los parámetros, solo lo que he usado. (Nota: agregar imágenes)

### Módulos

**-w**  especificar la WordList que usaremos para aplicar fuzz.

**-c** colorear los resultados, ayuda un poco a leer  de mejor manera. 

**--hc** ocultar códigos de estado como el 404 o el 500 (ejemplo: `--hc 404`).

**--sc** mostrar solo los códigos de estado que definamos (ejemplo: `--sc 200`)

**-t** especificar la cantidad de hilos que usaremos. Un ejemplo seria `-t 400` esto quiere decir que apicararemos 400 consultas simultaneas, este parámetro es usado para controlar la velocidad de consultas echas.

**-L** *follow http redirections*. Nos muestra las rutas directas y elimina las redirecciones.

**--sh** buscar por el tamaño de caracteres o de *chars*.

**--hl** buscas por el tamaño de lineas.

**-z** especificar un rango de numero para romper el *uid* como en siguiente ejemplo  `wfuzz -z range,0-999 http://www.ejemplo/index.php?uid=FUZZ`.

**-p** si usamos un proxy para navegar con este parámetro indicamos muestra ip y puerto(ejemplo: `-p 127.0.0.1:4000:TIPO`) los tipos son SOCK4, SOCKS5 o HTTP.

**-d** aplicar fuerza bruta a un login. Algunos ejemplos.

    username=FUZZ&password=FUZZ
    
    otro ejemplo:
    
    wffz -w UserList -w PwdList -d username=FUZZ&password=FUZZ 127.0.0.1/login.php

**-x** nos permite definir el método a ejecutar. (ejemplo: `GET, HEAD, POST, etc.. `).

  