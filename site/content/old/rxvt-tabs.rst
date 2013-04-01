Modificacion de rxvt-unicode con tabs
#####################################

:date: 2008-08-05 11:49:54
:tags: urxvt, sh

rxvt-unicode es un emulador de terminal muy bonito, lo que le
hacía falta era que pudiera tener tabs, buscando un poco en google se
encuentra que colocando **urxvt -pe tabbed** se puede tener tabs
los shorcuts son con Shift y las flechas:::


  Nuevo Tab                               Shift + Flecha Abajo
  Mover a la tab del lado derecho         Shift + Flecha Derecha
  Mover a la tab del lado izquierdo       Shift + Flecha Izquierda


Al probarlo se tiene problemas con las tildes y las ñ este problema
se soluciona cambiando el archivo */usr/lib/urxvt/perl/tabbed*
en la función **tab_key_press**, cambiaremos los shortcuts
parecidos a los de firefox o a los de gnome terminal::


  Se cambia:
  urxvt::ShiftMask   >   urxvt::ControlMask
  0xff51             >   0xff55
  0xff53             >   0xff56
  0xff54             >   0x74


Con esto la función queda de la siguiente manera::

  sub tab_key_press {
   my ($self, $tab, $event, $keysym, $str) = @_;

   if ($event->{state} & urxvt::ControlMask) {
      if ($keysym == 0xff55 || $keysym == 0xff56) {
         my ($idx) = grep $self->{tabs}[$_] == $tab, 0 .. $#{ $self->{tabs} };

         --$idx if $keysym == 0xff55;
         ++$idx if $keysym == 0xff56;

         $self->make_current ($self->{tabs}[$idx % @{ $self->{tabs}}]);

         return 1;
      } elsif ($keysym == 0x74) {
         $self->new_tab;

         return 1;
      }
   }
   elsif ($event->{state} & urxvt::ControlMask) {
      if ($keysym == 0xff55 || $keysym == 0xff56) {
         my ($idx1) = grep $self->{tabs}[$_] == $tab, 0 .. $#{ $self->{tabs} };
         my  $idx2  = ($idx1 + ($keysym == 0xff55 ? -1 : +1)) % @{ $self->{tabs} };

         ($self->{tabs}[$idx1], $self->{tabs}[$idx2]) =
            ($self->{tabs}[$idx2], $self->{tabs}[$idx1]);

         $self->make_current ($self->{tabs}[$idx2]);

         return 1;
      }
   }

   ()
  }


Esto permitirá tener nativamente tabs dentro de urxvt
