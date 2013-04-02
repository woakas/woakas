Montaje del Arduino
###################
:date: 2007-04-29 05:45:12
:lang: es
:tags: arduino

Desde hace dias habia comprado los componentes para el arduino y
gracias al enlace que dejo zea (http://randomlab.net) en uno de los
post pasados el montaje fue mucho mas facil. Quizas lo único que hace
falta allí es que despues del montaje uno debe incluir en la lista de
componente algunas resistencias y el conector de 25 pines para el
bootloader; gracias a mi hermano estas resistencias fueron
reemplazadas por algunos potenciometros y listo el montaje.

A la hora de de realizar el proceso del bootloder se probó sobre
windows XP y debian, en windows se debe tener un programa primero para
bajar el puerto paralelo, desafortunadamente en mi pc no funcionó, por
consiguiente no se pudo quemar el arduino en Debian, se siguió con el
manual que tiene la página oficial de `Arduino
<http://http://www.arduino.cc/playground/Linux/Debian>`_ y despues de
realizar todo el proceso el arduino tuvo un quemado satisfactorio.


El log que generá el arduino al colocar el bootloader es el siguiente
de esta forma se puede verificar que el arduino quedo con el
bootloader correctamente.

::
  
  Atmel AVR ATmega8 is found.
  Writing lock bits ...  Reinitializing device Atmel AVR ATmega8 is
  found.
  
  Lock Bits set to 0xff
  Atmel AVR ATmega8 is found.
  
  Fuse Low Byte set to 0xdf
  
  Fuse High Byte set to 0xca
  Atmel AVR ATmega8 is found.
  Erasing device ...
  Reinitializing device
  Atmel AVR ATmega8 is found.
  Uploading: flash
  Verifying: flash
  Atmel AVR ATmega8 is found.
  Writing lock bits ...
  Reinitializing device
  Atmel AVR ATmega8 is found.
  
  Lock Bits set to 0xcf
