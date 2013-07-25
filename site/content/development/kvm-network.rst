Configuración de Red con KVM y hetzner
######################################

:date: 2013-07-25 02:37
:email: woakas@gmail.com
:tags: kvm, hetzner

Luego de más de un año que teníamos con algunos compañeros un servidor
dedicado en suiza decidimos cambiar nuestro servidor a algo más
económico, tener un servidor en suiza tiene algunas ventajas:

* No revisan tu equipo.
* No monitorean tu tráfico.
* No se encuentra dentro de la unión europea osea que no tiene la
  obligación de cumplir normas de esta.


Pero algunas desventajas:

* El costo por un servidor dedicado en un datacenter de este país.
* La latencia hacia suramérica es un poco alta con un promedio de
  230ms.


Luego de que decidiéramos movernos escogimos a hetzner_ y se realizó
el proceso de migración, el servidor que se escogió es un ex10_ el
cual tiene muy buenas cosas como 64G de Ram y un procesador core i7
por tan solo 109 euros mensual.


Se solicitaron 8 ip adicionales para poder utilizar ip's fijas en las
máquinas virtuales que se tendrán allí. Luego se procedió a instalar
KVM y sus configuraciones.


Máquinas virtuales
__________________

El servidor dedicado usará KVM y alojará por lo pronto 5 máquinas
virtuales las cuales tendrán:

* 4 núcleos en el procesador
* 8G de ram cada una
* Disco duro qcow2 de 50G en la /
* IP fija
* Alguna otra solicitud de los dueños de la máquina virtual.


Red Macvtap (Fail)
__________________

Se realizó una configuración usando el módulo *macvtap* pero luego de
pelear mucho no funcionó con una buen performance, los routers de
hetzner no soportan *hairpin* por consiguiente las máquinas no se
podían ver entre ellas ni tampoco con el sistema host sin embargo
la configuración que se realizó es la siguiente::

  iface macvlan0 inet static
      address 78.X.X.1
      netmask 255.255.255.255
      pre-up ip link add link eth0 name macvlan0 type macvlan mode bridge
      post-up route add -host 78.X.X.2 dev macvlan0
      post-up route add -host 78.X.X.3 dev macvlan0
      post-up route add -host 78.X.X.4 dev macvlan0
      post-up route add -host 78.X.X.5 dev macvlan0
      post-up route add -host 78.X.X.6 dev macvlan0
      post-up route add -host 78.X.X.7 dev macvlan0
      post-down ip link del macvlan0


En cada uno de los guest se coloca la configuración::

  iface eth0 inet static
      address 78.X.X.2
      netmask 255.255.255.255
      gateway 78.46.X.1
      pointopoint 78.X.X.1


Luego de probar esta configuración los equipos se ven entre ellos y
con el host pero la tasa de upload es pésima no pasa de los 5K o 10K.


Red Bridge
__________

Luego de pelear mucho con el módulo de macvtap se puso en
funcionamiento en forma de bridge el cual no tiene mucho problema es
resulta fácil de configurar, la configuración del host es::

  iface virbr1 inet static
      address 78.X.X.1
      netmask 255.255.255.255
      bridge_ports none
      bridge_stp off
      bridge_fd 0
      bridge_maxwait 5
      pre-up brctl addbr virbr1
      post-up ip route add 78.X.X.2/32 dev virbr1
      post-up ip route add 78.X.X.3/32 dev virbr1
      post-up ip route add 78.X.X.4/32 dev virbr1
      post-up ip route add 78.X.X.5/32 dev virbr1
      post-up ip route add 78.X.X.6/32 dev virbr1
      post-up ip route add 78.X.X.7/32 dev virbr1



Las tasas de respuesta de subida y bajada del sistema son mas o menos
de 1M entre servidores de softlayer y amazon lo cual es muy estable.


.. _hetzner: http://www.hetzner.de/
.. _ex10: http://www.hetzner.de/hosting/produkte_rootserver/ex10
