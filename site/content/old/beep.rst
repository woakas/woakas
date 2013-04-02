Quitar el Altavoz del pc o beep
###############################
:date: 2007-08-30 22:44:23
:lang: es
:tags: linux

Recientemente un amigo de la universidad decidió instalar Lenny en un
portatil hewlett packard y tenía el inconveniente que sonaba el beep
por el altavoz en el portatil entoces despues de buscar por google
encontré algunas formas utiles de quitar este modulo:

* Primera es a una consola no grafica *(Ctrl+Alt+F1) xset -b*
* Otra opción es *rmmod pcspkr* o *modprobe -r pcspkr*

Se puede modificar el archivo .bashrc y se pone allí **set bell-style none** 

Estas opciones algunas solo son efectivas mientras no se apague el pc,
entonces para que sea permanente esta opción lo mejor es editar el
archivo **/etc/modprobe.d/pnp-hotplug** y comentar la linea que dice
*alias pnp:dPNP0800 pcspkr* con esto se aseguro que no se volvera a
cargar el modulo al inicio.
