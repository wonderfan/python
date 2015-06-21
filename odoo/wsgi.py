def application(environ, start_response):
    if config['proxy_mode'] and 'HTTP_X_FORWARDED_HOST' in environ:
        return werkzeug.contrib.fixers.ProxyFix(application_unproxied)(environ, start_response)
    else:
        return application_unproxied(environ, start_response)
        
def application_unproxied(environ, start_response):
    """ WSGI entry point."""
    # cleanup db/uid trackers - they're set at HTTP dispatch in
    # web.session.OpenERPSession.send() and at RPC dispatch in
    # openerp.service.web_services.objects_proxy.dispatch().
    # /!\ The cleanup cannot be done at the end of this `application`
    # method because werkzeug still produces relevant logging afterwards 
    if hasattr(threading.current_thread(), 'uid'):
        del threading.current_thread().uid
    if hasattr(threading.current_thread(), 'dbname'):
        del threading.current_thread().dbname

    with openerp.api.Environment.manage():
        # Try all handlers until one returns some result (i.e. not None).
        wsgi_handlers = [wsgi_xmlrpc]
        wsgi_handlers += module_handlers
        for handler in wsgi_handlers:
            result = handler(environ, start_response)
            if result is None:
                continue
            return result

    # We never returned from the loop.
    response = 'No handler found.\n'
    start_response('404 Not Found', [('Content-Type', 'text/plain'), ('Content-Length', str(len(response)))])
    return [response]        

root = Root()
openerp.service.wsgi_server.register_wsgi_handler(root)
