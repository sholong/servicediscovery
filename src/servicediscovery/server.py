# -*- coding:utf-8 -*-


from .core import ServiceDiscovery
from .core.ttypes import ServiceInfo
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


class ServiceHandler:
    def ping(self):
        return "yes"

    def sign_up(self, service_name, service_url, expire_s=None):
        return {"ret_code": 0, "ret_msg": u'服务注册成功',
                "data": {"service_name": service_name,
                         "service_url": service_url,
                         "expire": 10
                         }
                }

    def find_service(self, service_name):
        service_info = ServiceInfo()
        service_info.server_name = service_info
        service_info.server_url = "http://www.baidu.com"
        service_info.expire_s = 10
        return service_info


def server_init(service_ip='localhost', service_port='9090'):
    handler = ServiceHandler()
    processor = ServiceDiscovery.Processor(handler)
    transport = TSocket.TServerSocket(service_ip, service_port)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()
    server = TServer.TSimpleServer(processor, transport,
                                   tfactory, pfactory)
    return server
