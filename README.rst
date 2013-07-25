Woakas Blog
===========

Sources for http://woakas.pehik.co


Compile and Install
-------------------

Install dependences::

    pip install -r requirements.pip


Initialize submodules for install pelican-plugins in the root path repository::

    git submodule init
    git submodule update


then compile::

    cd site; make html

Preview the output in http://localhost:8000/::

    cd output; python -m SimpleHTTPServer
