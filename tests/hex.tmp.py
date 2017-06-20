def test_hex_on_int_type():
    print __call_method_0(__call(hex,__call_cls_builtin(int, 0)).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call(hex,__call_cls_builtin(int, 1)).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call(hex,__call_cls_builtin(int, 5)).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call(hex,__call_cls_builtin(int, 15)).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call(hex,__call_cls_builtin(int, 16)).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call(hex,__call_cls_builtin(int, 32)).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call(hex,__call_cls_builtin(int, 1024)).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call(hex,__call_method_0(__call_cls_builtin(int, 6).__neg__)).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call(hex,__call_method_0(__call_cls_builtin(int, 16).__neg__)).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call(hex,__call_method_0(__call_cls_builtin(int, 32).__neg__)).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call(hex,__call_method_0(__call_cls_builtin(int, 1024).__neg__)).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call(hex,__call_method_1(__call_method_0(__call_cls_builtin(int, 1024).__neg__).__mul__, __call_cls_builtin(int, 1024))).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call(hex,True).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call(hex,False).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    return None

def test_hex_on_custom_type():
    class MyObject:
        def __init__(self, x):
            self.x = x

            return None

        def __hex__(self):
            return __call(self.x.__str__)

            return None


    print __call_method_0(__call(hex,__call(MyObject,__call_cls_builtin(int, 0))).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call(hex,__call(MyObject,__call_cls_builtin(int, 5))).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call(hex,__call(MyObject,__call_cls_builtin(int, 16))).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call(hex,__call(MyObject,__call_cls_builtin(int, 32))).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call(hex,__call(MyObject,__call_cls_builtin(int, 1024))).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call(hex,__call(MyObject,__call_method_0(__call_cls_builtin(int, 16).__neg__))).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    print __call_method_0(__call(hex,__call(MyObject,__call_method_0(__call_cls_builtin(int, 256).__neg__))).__str__)
    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
    return None

def test_hex_on_unsupported_types():
    def test_hex_with_typeerror(x):
        try:
            print __call_method_0(__call(hex,x).__str__)
            print __call_method_0(__call_cls_builtin(str, "\n").__str__)
        except TypeError:
            print __call_method_0(__call_method_1(__call_cls_builtin(str, "Expected TypeError for calling hex() on ").__add__, __call(x.__str__)).__str__)
            print __call_method_0(__call_cls_builtin(str, "\n").__str__)

        return None

    __call(test_hex_with_typeerror,__call_cls_builtin(str, "5"))
    __call(test_hex_with_typeerror,__call_cls_builtin(str, "32"))
    __call(test_hex_with_typeerror,__call_cls_builtin(str, "32.0"))
    __call(test_hex_with_typeerror,__call(list,__call_cls_builtin(list, [__call_cls_builtin(int, 1), __call_cls_builtin(int, 2), __call_cls_builtin(int, 3)])))
    return None

__call(test_hex_on_int_type)
__call(test_hex_on_custom_type)
__call(test_hex_on_unsupported_types)