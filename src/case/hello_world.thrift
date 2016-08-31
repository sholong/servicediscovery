struct StructT {
    1: required i32 id,
    2: required string name,
}

service HelloWorld {
    string ping(),
    string say(1:string msg),
    list<string> func_ret_list(),
    set<string> func_ret_set(),
    map<string,string> func_ret_map(),
    StructT func_ret_struct(),
}