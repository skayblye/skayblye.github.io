---
layout: post
title: Anonsurf me dejo sin internet
date: 2022-08-31
modified: 2022-08-31
description: Tuve una especie de error al probar anonsurf, te cuento lo que paso, como lo agregle y por que paso.
tag:
 - linux
 - herramientas
 - problemas
---

Hace días tuve algo de curiosidad por algunas herramientas que cuenta parrot os, ya que en serio cuenta con cientos, estuve viendo algunas y entre ellas estaba anonsurf.

Muy lindo el cambio de ip, eso de poder habilitarlo desde el arranque del sistema, etc. El mayor problema fue cuando lo apague; rápidamente me di cuenta que no contaba con internet. O bueno algo así.

![imagen 1](https://raw.githubusercontent.com/skayblye/skayblye.github.io/master/_posts/sin-internet-anonsurf/zero.png)

El error que me mostraba no era directamente sin conexión, era un error diciéndome que no podía conectarse con el servidor y así con cada página que visitaba. Entonces se me ocurrió volver a encender Anonsuft de nuevo y sorpresa!!.

![imagen 2](https://raw.githubusercontent.com/skayblye/skayblye.github.io/master/_posts/sin-internet-anonsurf/zero1.png)

De nuevo tenemos internet, Pero hay un detalle…Seguimos por la red tor, si nos desconectamos de nuevo no tendremos internet.

para arreglar esto tendremos que instalar un paquete llamado resolvconf, es tan simple como hacer un apt install.

    sudo apt install resolvconf 

Pero un detalle, tendremos que descargarlo conectados por anonsurf, en caso de no estar conectados los repos tampoco nos funcionaran.

![imagen 3](https://raw.githubusercontent.com/skayblye/skayblye.github.io/master/_posts/sin-internet-anonsurf/zero2.png)
![imagen 4](https://raw.githubusercontent.com/skayblye/skayblye.github.io/master/_posts/sin-internet-anonsurf/zero3.png)

En caso que este paquete ya esté instalado(dudo que sea el caso). Tendríamos que borrarlo y volver a instalar.

    sudo apt remove –purge resolvconf && sudo apt install resolvconf 

Una vez hecho esto, apagaremos anonsurf y reiniciamos el sistema, al encenderlo de nuevo ya deberíamos tener el internet de regreso.

![imagen 5](https://raw.githubusercontent.com/skayblye/skayblye.github.io/master/_posts/sin-internet-anonsurf/zero4.png)

### Pero…¿por qué se fue en primer lugar?

Al activar anonsurf nos borro un archivo muy importante localizado en etc con el nombre de resolv.conf. Pueden ver que contiene este archivo haciendo un cat.

    cat /etc/resolv.conf

Un ejemplo: 

![imagen 6](https://raw.githubusercontent.com/skayblye/skayblye.github.io/master/_posts/sin-internet-anonsurf/Selecci%C3%B3n_003.png)

Este pequeño archivo está presente en la mayoría de sistemas y es el encargado de configurar la resolución de nombres de dominio. Por esa razón nos decía que no podía encontrar el servidor.
