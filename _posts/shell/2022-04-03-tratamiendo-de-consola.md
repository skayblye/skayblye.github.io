---
layout: post
title: Tratamiento de la consola (reverse shell)
date: 2022-04-03
modified: 2022-04-03
description: Es el procedimiento para obtener una consola funcional al obtener una reverse shell
tag:
 - pentesting
 - linux
 - ctf
 - shell
---
Cuando ganamos acceso al sistema con una reverse shell nos encontraremos que muchas cosas no funcionan correctamente, como el **CTRL + L** que limpia la consola, las proporciones o los teclas para moverlos al inicio y al final. 

Para arreglar esto de manera rápida podríamos solo hacer que python nos de una ejecutando lo siguiente. 

    python -c 'import pty; pty.spawn("/bin/bash")'

### Segundo metodo

Pero en ocasiones no funciona del todo bien, así que podemos hacerlo de la manera larga.

    script /dev/null -c bash
   
  Hacemos **CTRL +Z** para poner en pausa la cesión que tenemos activa, esto no llevara de nuevo a nuestra consola en la cual escribimos.

    stty raw -echo; fg

Ahora nos mandara de nuevo a nuestra cesión en pausa, en la cual no nos aparecerá nada pero podremos escribir, así que escribimos `reset xterm`  nos reiniciara la consola y mas o menos esta funcional pero igual hay que hacer unos pasos extras para que funcione del todo, lo siguiente seria cambiar las variables de entorno para que nos funcionen lo atajos del teclado. 

    export TERM=xterm
    
    export SHELL=bash

Para arreglar los tamaños y proporciones, desde otra consola de preferencia abierta en pantalla completa escribimos `stty size`y nos dará el numero de filas y columnas. Sabiendo el numero de filas y columnas nos vamos a nuestra reverse shell y escribimos `stty rows 43 columns 180`   .

 Ahora tendremos una shell completamente funcional y aunque es un método mas largo es que el que menos me da errores. 