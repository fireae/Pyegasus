def test_hasattr_on_builtin_types():
    if __call(__call_cls_1(bool, __call(hasattr,__call_cls_builtin(int, 1), __call_cls_builtin(str, "__pos__"))).__not__):
        raise __call_cls_0(AssertionError)
    if __call(__call_cls_1(bool, __call(hasattr,__call_cls_builtin(float, 3.1415), __call_cls_builtin(str, "__mul__"))).__not__):
        raise __call_cls_0(AssertionError)
    if __call(__call_cls_1(bool, __call(hasattr,__call_cls_builtin(str, "Hello world"), __call_cls_builtin(str, "__str__"))).__not__):
        raise __call_cls_0(AssertionError)
    if __call(__call_cls_1(bool, __call(hasattr,__call(set,__call_cls_builtin(set, {__call_cls_1(set.__set_Item, __call_cls_builtin(int, 1)), __call_cls_1(set.__set_Item, __call_cls_builtin(int, 2)), __call_cls_1(set.__set_Item, __call_cls_builtin(int, 3))})), __call_cls_builtin(str, "symmetric_difference"))).__not__):
        raise __call_cls_0(AssertionError)
    if __call(__call_cls_1(bool, __call_method_1(__call(hasattr,__call_cls_builtin(int, 3), __call_cls_builtin(str, "__compute__")).__eq__, False)).__not__):
        raise __call_cls_0(AssertionError)
    if __call(__call_cls_1(bool, __call_method_1(__call(hasattr,__call_cls_builtin(float, 0.001), __call_cls_builtin(str, "sqrt")).__eq__, False)).__not__):
        raise __call_cls_0(AssertionError)
    if __call(__call_cls_1(bool, __call_method_1(__call(hasattr,__call_cls_builtin(list, [__call_cls_builtin(int, 1), __call_cls_builtin(int, 2), __call_cls_builtin(int, 3)]), __call_cls_builtin(str, "erase")).__eq__, False)).__not__):
        raise __call_cls_0(AssertionError)
    if __call(__call_cls_1(bool, __call(hasattr,object, __call_cls_builtin(str, "__new__"))).__not__):
        raise __call_cls_0(AssertionError)
    if __call(__call_cls_1(bool, __call(hasattr,int, __call_cls_builtin(str, "__neg__"))).__not__):
        raise __call_cls_0(AssertionError)
    if __call(__call_cls_1(bool, __call(hasattr,dict, __call_cls_builtin(str, "__getitem__"))).__not__):
        raise __call_cls_0(AssertionError)
    if __call(__call_cls_1(bool, __call_method_1(__call(hasattr,str, __call_cls_builtin(str, "__tostring__")).__eq__, False)).__not__):
        raise __call_cls_0(AssertionError)
    if __call(__call_cls_1(bool, __call_method_1(__call(hasattr,complex, __call_cls_builtin(str, "__simplify__")).__eq__, False)).__not__):
        raise __call_cls_0(AssertionError)
    if __call(__call_cls_1(bool, __call_method_1(__call(hasattr,bool, __call_cls_builtin(str, "__truthy__")).__eq__, False)).__not__):
        raise __call_cls_0(AssertionError)
    return None

def test_hasattr_on_custom_type():
    class MyObject:
        def __init__(self):
            self.value = __call_cls_builtin(int, 5)

            return None

        def hello_world(self):
            print __call_method_0(__call_cls_builtin(str, "Hello").__str__)
            print __call_method_0(__call_cls_builtin(str, "\n").__str__)
            return None


    if __call(__call_cls_1(bool, __call(hasattr,MyObject, __call_cls_builtin(str, "__init__"))).__not__):
        raise __call_cls_0(AssertionError)
    if __call(__call_cls_1(bool, __call(hasattr,MyObject, __call_cls_builtin(str, "hello_world"))).__not__):
        raise __call_cls_0(AssertionError)
    if __call(__call_cls_1(bool, __call_method_1(__call(hasattr,MyObject, __call_cls_builtin(str, "value")).__eq__, False)).__not__):
        raise __call_cls_0(AssertionError)
    o = __call(MyObject)

    if __call(__call_cls_1(bool, __call(hasattr,o, __call_cls_builtin(str, "__init__"))).__not__):
        raise __call_cls_0(AssertionError)
    if __call(__call_cls_1(bool, __call(hasattr,o, __call_cls_builtin(str, "hello_world"))).__not__):
        raise __call_cls_0(AssertionError)
    if __call(__call_cls_1(bool, __call(hasattr,o, __call_cls_builtin(str, "value"))).__not__):
        raise __call_cls_0(AssertionError)
    return None

__call(test_hasattr_on_builtin_types)
__call(test_hasattr_on_custom_type)