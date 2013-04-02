Resetar WRT54GL + freifunk
##########################
:date: 2007-08-28 00:09:15
:lang: es
:tags: linux, Freifunk

Bueno ya despues de estar cacharreando con Freifunk sucedió que
coloque alguna opción que no debí haber puesto y mi router quedo
aislado, no respondía el ping tampoco al realizar un nmap a la ip y
tampoco el DHCP funcionaba, despues de buscar un poco encontre esto en
http://www.slcolombia.org/RedesInalambricas el cual me ayudo a
resetear mi AP de forma correcta simplemente se siguen los siguientes
pasos y listo problema sulucionado

* Se desconecta el cable de poder.
* Se espera a que el led que dice "dmz" se inicie
* Se presiona reset durante aproximadamente dos segundos.
* Si el proceso ha salido bien el led "dmz" empezará a parpadear 3
  veces cada segundo. Cuando esté en este estado es posible usar las
  configuraciones originales y, por ejemplo, acceder a la interface de
  administración entrando a la dirección: http://192.168.1.1
