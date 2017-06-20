def test_id_on_objects_of_same_type():
    print __call_method_0(__call_method_1(__call(id,__call_cls_builtin(int, 1)).__ne__, __call(id,__call_cls_builtin(int, 2))).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call_method_1(__call(id,__call_cls_builtin(float, 3.14)).__ne__, __call(id,__call_cls_builtin(float, 3.14000001))).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call_method_1(__call(id,__call_cls_builtin(str, "Hello")).__ne__, __call(id,__call_cls_builtin(str, "world"))).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call_method_1(__call(id,__call(list,__call_cls_builtin(list, [__call_cls_builtin(int, 1), __call_cls_builtin(int, 2), __call_cls_builtin(int, 3)]))).__ne__, __call(id,__call(list,__call_cls_builtin(list, [__call_cls_builtin(int, 1), __call_cls_builtin(int, 2), __call_cls_builtin(int, 3)])))).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call_method_1(__call(id,__call(set,__call_cls_builtin(set, {__call_cls_1(set.__set_Item, __call_cls_builtin(str, "a")), __call_cls_1(set.__set_Item, __call_cls_builtin(str, "b")), __call_cls_1(set.__set_Item, __call_cls_builtin(str, "c"))}))).__ne__, __call(id,__call(set,__call_cls_builtin(set, {__call_cls_1(set.__set_Item, __call_cls_builtin(str, "a")), __call_cls_1(set.__set_Item, __call_cls_builtin(str, "b")), __call_cls_1(set.__set_Item, __call_cls_builtin(str, "c"))})))).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call_method_1(__call(id,__call(dict,__call_cls_builtin(dict, {
        __call_method_0(__call_cls_builtin(int, 1).__hash__): __call_cls_2(dict.__dict_KeyValuePair, __call_cls_builtin(int, 1), __call_cls_builtin(int, 1)),
        __call_method_0(__call_cls_builtin(int, 2).__hash__): __call_cls_2(dict.__dict_KeyValuePair, __call_cls_builtin(int, 2), __call_cls_builtin(int, 2)),
}))).__ne__, __call(id,__call(dict,__call_cls_builtin(dict, {
        __call_method_0(__call_cls_builtin(int, 1).__hash__): __call_cls_2(dict.__dict_KeyValuePair, __call_cls_builtin(int, 1), __call_cls_builtin(int, 1)),
        __call_method_0(__call_cls_builtin(int, 2).__hash__): __call_cls_2(dict.__dict_KeyValuePair, __call_cls_builtin(int, 2), __call_cls_builtin(int, 2)),
})))).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    return None

def test_id_on_objects_of_different_types():
    print __call_method_0(__call_method_1(__call(id,__call_cls_builtin(int, 1)).__ne__, __call(id,__call_cls_builtin(str, "1"))).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call_method_1(__call(id,__call_cls_builtin(int, 0)).__ne__, __call(id,__call_cls_builtin(float, 0.0))).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call_method_1(__call(id,__call(list,__call_cls_builtin(list, [__call_cls_builtin(int, 1), __call_cls_builtin(int, 2), __call_cls_builtin(int, 3)]))).__ne__, __call(id,__call(tuple,__call_cls_builtin(list, [__call_cls_builtin(int, 1), __call_cls_builtin(int, 2), __call_cls_builtin(int, 3)])))).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    return None

def test_id_on_type_objects():
    print __call_method_0(__call_method_1(__call(id,object).__eq__, __call(id,object)).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call_method_1(__call(id,int).__eq__, __call(id,int)).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call_method_1(__call(id,float).__eq__, __call(id,float)).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call_method_1(__call(id,str).__eq__, __call(id,str)).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call_method_1(__call(id,dict).__eq__, __call(id,dict)).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call_method_1(__call(id,int).__ne__, __call(id,object)).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call_method_1(__call(id,int).__ne__, __call(id,float)).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call_method_1(__call(id,list).__ne__, __call(id,tuple)).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call_method_1(__call(id,list).__ne__, __call(id,set)).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call_method_1(__call(id,set).__ne__, __call(id,dict)).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    return None

def test_id_on_custom_type():
    class MyObject:
        def __init__(self):
            pass
            return None


    print __call_method_0(__call_method_1(__call(id,MyObject).__ne__, __call(id,object)).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call_method_1(__call(id,MyObject).__eq__, __call(id,MyObject)).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    o = __call(MyObject)

    print __call_method_0(__call_method_1(__call(id,__call(MyObject)).__ne__, __call(id,o)).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    return None

__call(test_id_on_objects_of_same_type)
__call(test_id_on_objects_of_different_types)
__call(test_id_on_type_objects)
__call(test_id_on_custom_type)