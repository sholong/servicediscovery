# -*- coding:utf-8 -*- 
#!/usr/bin/env python

import socket
import sys
sys.path.append('./gen-py')

from hello_world import HelloWorld
from hello_world.ttypes import StructT

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


class HelloWorldHandler:
    def ping(self):
        return "pong"

    def say(self, msg):
        ret = "Received: " + msg
        print ret
        return ret

    def func_ret_list(self):
        return ['1', '2']

    def func_ret_set(self):
        return ('1', '2', '3')

    def func_ret_map(self):
        return {'id': '1'}

    def func_ret_struct(self):
        struct_t = StructT()
        struct_t.id = 1
        struct_t.name = u'zhangsan'
        return struct_t

handler = HelloWorldHandler()
processor = HelloWorld.Processor(handler)
transport = TSocket.TServerSocket("localhost", 9090)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print "Starting thrift server in python..."
server.serve()
print "done!"
