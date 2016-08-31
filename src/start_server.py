# -*- coding:utf-8 -*-

from servicediscoveryt.server import server_init


server = server_init()
print 'start server...'
server.serve()
