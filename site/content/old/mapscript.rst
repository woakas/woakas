Mapserver + Mapscript + web.py
##############################

:date: 2010-01-22 09:54:58
:lang: es
:category: development
:tags: web.py, python

Recientemente he utilizado mapscript con web.py para generar mapas que
sean generados en tiempo de ejecución, esta porción de código permite
leer archivos .map y luego se renderizan con las opciones habituales
de mapserver para WMS, el método POST adiciona algunas lines para
permitir el uso de un servicio WFS dentro de mapserver.

Se puede utilizar jinja2 o algún otro manejador de templates para
cambiar el .map en tiempo de ejecución y de esta forma poder enviar
algún parámetro adicional para realizar cambios en el servicio WMS o
WFS.


.. code:: python

    import web
    import mapscript
    
    
    # URLS
    urls = (
        '/','Basic',
    )
    
    def info_layer(cls):
        aux=''
        pathUrl=str(web.ctx.realhome+web.ctx.path)
        web.header("Content-Type","text/html; charset=utf-8")
        aux+='<b>Description: </b>%s<br>' % (str(cls.__doc__))
        aux+='<b>Capabilities WMS: </b><a href="%s?SERVICE=wms&REQUEST=GetCapabilities&VERSION=1.1.1&REQUEST=GetCapabilities">%s</a><br>'%(pathUrl,pathUrl)
        aux+='<b>Checker WMS FGDC: </b><a href="http://registry.fgdc.gov/statuschecker/services/rest/index.php?url=%s?SERVICE=wms&REQUEST=GetCapabilities&VERSION=1.1.1&type=wms&formattype=html">%s</a><br>'%(str(web.ctx.realhome+web.ctx.path),str(web.ctx.path))
    
        return aux
    
    class Basic:
        """Layers Basics
        """
        def GET(self):
            
            vars = web.input()
            if len(vars)==0:
                return info_layer(Basic)
            req = mapscript.OWSRequest()
            for i in vars.keys():
                req.setParameter( i, vars[i])
    
                                 
            map = mapscript.mapObj('basic.map')
            
            mapscript.msIO_installStdoutToBuffer()
            map.OWSDispatch( req )
    
            content_type = mapscript.msIO_stripStdoutBufferContentType()
            content = mapscript.msIO_getStdoutBufferBytes()
            web.header("Content-Type","%s; charset=utf-8"%(content_type))
            return content
    
    
        def POST(self):
             
            vars = web.input()
            req = mapscript.OWSRequest()
            for i in vars.keys():
                req.setParameter( i, vars[i])
            
            req.postrequest=web.data()
            req.type=mapscript.MS_POST_REQUEST
            map = mapscript.mapObj('basic.map')
           
            mapscript.msIO_installStdoutToBuffer()
            map.OWSDispatch( req )
    
            content_type = mapscript.msIO_stripStdoutBufferContentType()
            content = mapscript.msIO_getStdoutBufferBytes()
            web.header("Content-Type","%s; charset=utf-8"%(content_type))
            return content
    
    app = web.application(urls, globals())
    
    #web.internalerror = web.debugerror 
    
    
    if __name__ == "__main__":
        app.run()
