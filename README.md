# servicediscovery 服务发现 持续更新中
thrift+python+redis 实现

## thrift 安装

参考官网的安装方法： http://thrift.apache.org/docs/install/centos

## python 安装

参考：

## python thrift 包安装

pip install thrift 或者 conda install thrift

## 编写thrift IDL文档

```python
/* 命名空间--python中module名称 */
namespace py core

/* 定义结构体---python 中的类， 结构体中的元素相当于类的属性
   格式：
   元素位置: 比传/非必传 数据类型 变量名称
   required--必传， optional--可选的
*/
struct ServiceInfo {
    1: required string server_name;
    2: required string server_url;
    3: optional i32 expire_s;
}

/* 定义远程方法 */
service ServiceDiscovery {
    string ping(),
    map<string, string> sign_up(1: string service_name, 2: string service_url, 3: string expire_s),
    ServiceInfo find_service(1: string service_name),
}
```

详情见文档: http://github.com/kiyoa/servicediscovery

## 使用thrift生成python服务库

thrift -r --gen py core.thrift






