namespace py core

struct ServiceInfo {
    1: required string server_name;
    2: required string server_url;
    3: optional i32 expire_s;
}

service ServiceDiscovery {
    string ping(),
    map<string, string> sign_up(1: string service_name, 2: string service_url, 3: string expire_s),
    ServiceInfo find_service(1: string service_name),
}