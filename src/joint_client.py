# -*- coding:utf-8 -*-

from servicediscoveryt.core import ServiceDiscovery
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:
    transport = TSocket.TSocket('localhost', 9090)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = ServiceDiscovery.Client(protocol)
    transport.open()

    print "client - ping"
    print "server - " , client.ping()
    print "client - sign up service"
    print "server - ", client.sign_up('recharge', 'http://www.baidu.com', '10')
    print "client - find service"
    print "server - ", client.find_service('recharge')

    transport.close()

except Thrift.TException, ex:
    print "%s" % (ex.message)
