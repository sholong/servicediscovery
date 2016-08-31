#!/usr/bin/env python

import sys
sys.path.append('./gen-py')

from hello_world import HelloWorld
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:
    transport = TSocket.TSocket('localhost', 9090)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = HelloWorld.Client(protocol)
    transport.open()

    print "client - ping"
    print "server - " + client.ping()

    print "client - say"
    msg = client.say("Hello!")
    print "server - " + msg
    print "client - func_ret_list"
    ret = client.func_ret_list()
    print ret, type(ret)
    print "client - func_ret_set"
    ret = client.func_ret_set()
    print ret, type(ret)
    print "client - func_ret_map"
    ret = client.func_ret_map()
    print ret, type(ret)
    print "client - func_ret_struct"
    ret = client.func_ret_struct()
    print ret, type(ret)

    transport.close()

except Thrift.TException, ex:
    print "%s" % (ex.message)
