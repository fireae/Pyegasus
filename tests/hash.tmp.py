def test_hash_on_int_type():
    print __call_method_0(__call(hash,__call_cls_builtin(int, 0)).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call_method_1(__call(hash,__call_cls_builtin(int, 1)).__gt__, __call_cls_builtin(int, 0)).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call_method_1(__call(hash,__call_cls_builtin(int, 0)).__eq__, __call(hash,__call_cls_builtin(int, 0))).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call_method_1(__call(hash,__call_cls_builtin(int, 0)).__ne__, __call(hash,__call_cls_builtin(int, 1))).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    return None

def test_hash_on_float_type():
    print __call_method_0(__call(hash,__call_cls_builtin(float, 0.0)).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call_method_1(__call(hash,__call_cls_builtin(float, 0.1)).__gt__, __call_cls_builtin(int, 0)).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call_method_1(__call(hash,__call_cls_builtin(float, 3.14)).__ne__, __call(hash,__call_cls_builtin(int, 3))).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call_method_1(__call(hash,__call_cls_builtin(float, 3.14)).__ne__, __call(hash,__call_cls_builtin(float, 3.0))).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    return None

def test_hash_on_str_type():
    print __call_method_0(__call_method_1(__call(hash,__call_cls_builtin(str, "")).__gte__, __call_cls_builtin(int, 0)).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call_method_1(__call(hash,__call_cls_builtin(str, "1")).__ne__, __call(hash,__call_cls_builtin(int, 1))).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call_method_1(__call(hash,__call_cls_builtin(str, "Hello")).__ne__, __call(hash,__call_cls_builtin(str, "hello"))).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call_method_1(__call(hash,__call_cls_builtin(str, "Hello")).__ne__, __call(hash,__call_cls_builtin(str, "World"))).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    return None

def test_hash_on_custom_type():
    class MyObject:
        def __init__(self):
            pass
            return None


    o = __call(MyObject)

    print __call_method_0(__call_method_1(__call(hash,o).__gt__, __call_cls_builtin(int, 0)).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call_method_1(__call(hash,o).__eq__, __call(hash,o)).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    o2 = __call(MyObject)

    print __call_method_0(__call_method_1(__call(hash,o).__ne__, __call(hash,o2)).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    class YourObject:
        def __init__(self):
            pass
            return None

        def __hash__(self):
            return __call_cls_builtin(int, 5)

            return None


    o = __call(YourObject)

    print __call_method_0(__call(hash,o).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call_method_1(__call(hash,__call(YourObject)).__eq__, __call(hash,o)).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call_method_1(__call(hash,__call(YourObject)).__ne__, __call(hash,__call(MyObject))).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    return None

__call(test_hash_on_int_type)
__call(test_hash_on_float_type)
__call(test_hash_on_str_type)
__call(test_hash_on_custom_type)