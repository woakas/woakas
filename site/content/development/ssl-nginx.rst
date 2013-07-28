Configuración de SSL en Nginx
######################################

:date: 2013-07-28 02:16
:email: woakas@pehik.co
:tags: ssl, nginx


Al realizar la instalación de un certificado SSL siempre tengo algunas
dudas sobre como optimizar el sitio, que tipos de cifrado dejo activos
o los protocolos permitidos y luego de buscar un poco llegué a la
siguiente configuración la cual permite tener un buen performance y
certificado asegurado::

    # SSL
    ssl_certificate /etc/nginx/ssl/domain.pem;
    ssl_certificate_key /etc/nginx/ssl/domain.key;
    ssl_protocols SSLv3 TLSv1 TLSv1.1 TLSv1.2;
    ssl_ciphers ECDHE-RSA-AES128-SHA256:AES128-GCM-SHA256:RC4:HIGH:!MD5:!aNULL:!EDH;
    ssl_prefer_server_ciphers on;
    ssl_session_cache    shared:SSL:10m;
    ssl_session_timeout  10m;


Con esta configuración y usando la utilidad para pruebas de ssllabs_
alcanzamos una clasificación tipo A, con esto podemos estar seguros
que nuestro servidor no tiene algún método de cifrado un poco inseguro
o algún ataque a la fecha que pueda llegar a ser vulnerable.

.. image:: |filename|/static/images/ssl.png
   :scale: 80 %
   :alt: ssllabs
   :align: center



.. _ssllabs: http://ssllabs.com/ssltest/analyze.html
