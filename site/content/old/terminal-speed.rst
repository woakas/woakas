Test de Velocidad a la terminal
###############################

:date: 2009-07-21 10:32:06
:tags: terminal

Luego de probar varios emuladores de terminal he escogido
`urxvt <http://software.schmorp.de/pkg/rxvt-unicode.html>`_ debido a su
rapidez y su soporte para Unicode. Realice la siguiente prueba para
comprobar la velocidad del scrolling de algunos de los emuladores de
terminal mas conocidos, aquí estan los resultados:

En todos los emuladores se coloco la siguiente instrucción::

    time seq -f 'teeeeeeeeeeeeeeeeeeeeeeeeeeeeeest %g' 1000000

Y los resultados son los siguientes::


  ### gnome-terminal
      real     1m30.059s
      user     0m0.664s
      sys      0m0.660s
  
  
  ### urxvt
      real     0m3.886s
      user     0m1.132s
      sys      0m1.784s
  
  
  ### urxt + screen
      real    0m13.204s
      user    0m1.172s
      sys     0m1.096s
  
  
  ### xterm
      real    0m40.119s
      user    0m1.172s
      sys     0m1.032s
  
  ### konsole
      real    0m5.947s
      user    0m1.144s
      sys     0m1.064s


como se ve el más rápido de todos es **urxvt** seguido de **konsole**.
