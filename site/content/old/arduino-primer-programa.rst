Primer programa del Arduino
###########################
:date: 2007-05-26 11:07:03
:lang: es
:tags: arduino

Bueno despues de tener el arduino montado y con el bootloader uno debe
montar la parte de la conexión serial para ello muchos de los cables
del mouse que son seriales (no ps/2) vienen ya con los tres cables
listos que nesesitamos, por ello si uno tiene un mouse que pueda dañar
sería lo recomendable para esta labor.

Al tener listo el puerto Serial ya esta listo para realizar una prueba
del funcionamiento para esto abrimos el software del arduino nos
dirigimos a *file > Sketchbook > Examples > led_blink* este programa
simplemente hará que prenda y apague el led en el pin 13 (Led que se
encuentra conectado en la protoboard)

::
  
  int ledPin = 13; //
  LED connected to digital pin 13
  
  void setup()
  {
    pinMode(ledPin, OUTPUT);      // sets the digital pin as output
  }
  
  void loop()
  {
    digitalWrite(ledPin, HIGH);   // sets the LED on
    delay(1000);                  // waits for a second
    digitalWrite(ledPin, LOW);    // sets the LED off
    delay(1000);                  // waits for a second
  }
