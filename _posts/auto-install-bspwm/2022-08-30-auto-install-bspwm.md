---
layout: post
title: Hice un Script que instala todo Bspwm
date: 2022-08-30
modified: 2022-08-30
description: Esplicacion de la herramienta auto-install-bspwm echa en python 3 para facilitar la instalacion y configuracion. 
tag:
 - linux
 - herramientas
 - bspwm
---

Desde hace tiempo llevo usando Bspwm y me ha agradado bastante, es muy cómodo al momento de trabajar con múltiples herramientas. Y con el paso del tiempo he ido modificando diferentes configuraciones.

Empezando con un video de **s4vitar**, en específico, [Cómo configurar un buen entorno de trabajo en Linux](https://www.youtube.com/watch?v=MF4qRSedmEs), En ese tiempo llevaba poco usando linux así que fue fascinante para mi el nivel de personalización que podría alcanzar.

Actualmente sigo usando bspwm pero con configuraciones algo más a mi gusto personal y más pulidas. 

![imagen 1](zero1.png?msec=1661902386009)

![imagen 2](zero3.png?msec=1661902386004)

Pero me di cuenta que lleva bastante tiempo instalarlo todo, aunque sepas cada cosa que tienes que tocar, resulta bastante tardado, por eso primero opté por hacer un repo con mis archivos pero igual era algo lento, sin contar que no me agradaba mucho. Al final pensé que era una buena manera de practicar, mejorar mi configuracion e instalarlo mas rapido.

El script al ejecutarlo tiene solo tres opciones actualmente, la primera parte internamente instala y configura todo lo que necesita del usuario root. La segunda solo mueve carpetas y archivos de configuración a sus respectivos lugares. 

![imagen 3](zero10.png?msec=1661902798891)

![imagen 4](zero11.png?msec=1661902829284)

![imagen 5](zero12.png?msec=1661902863110)

![imagen 6](zero13.png?msec=1661902927124)

Este script sigue en una fase algo temprana pero es funcional, me di cuenta que tiene más potencial.

A futuro iré actualizando para meterle más opciones y más temas. Por si alguien está interesado en el auto install les dejo el repo [aqui](https://github.com/skayblye/auto-install-bspwm).