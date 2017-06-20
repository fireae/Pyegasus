def test_if():
    def test_if_inner(x):
        if x:
            print __call_method_0(__call_cls_builtin(str, "True").__str__)
            print __call_method_0(__call_cls_builtin(str, "\n").__str__)

        return None

    __call(test_if_inner,__call_cls_builtin(int, 1))
    __call(test_if_inner,__call_method_1(__call_cls_builtin(int, 1).__add__, __call_cls_builtin(int, 2)))
    __call(test_if_inner,True)
    return None

def test_if_else():
    def test_if_else_inner(x):
        if x:
            print __call_method_0(__call_cls_builtin(str, "True").__str__)
            print __call_method_0(__call_cls_builtin(str, "\n").__str__)
        else:
            print __call_method_0(__call_cls_builtin(str, "False").__str__)
            print __call_method_0(__call_cls_builtin(str, "\n").__str__)

        return None

    __call(test_if_else_inner,__call_cls_builtin(int, 1))
    __call(test_if_else_inner,__call_cls_builtin(int, 0))
    __call(test_if_else_inner,True)
    __call(test_if_else_inner,False)
    __call(test_if_else_inner,__call_method_1(__call_cls_builtin(int, 0).__pow__, __call_cls_builtin(int, 2)))
    __call(test_if_else_inner,__call_method_1(__call_cls_builtin(int, 0).__div__, __call_cls_builtin(int, 2)))
    __call(test_if_else_inner,(__call_cls_builtin(int, 1) or __call_cls_builtin(int, 0)))
    __call(test_if_else_inner,(True and False))
    return None

def test_if_elif_else():
    def test_if_elif_else_inner(x):
        if __call_method_1(__call_method_1(x.__mod__, __call_cls_builtin(int, 2)).__eq__, __call_cls_builtin(int, 0)):
            print __call_method_0(__call_cls_builtin(str, "X is a multiple of 2").__str__)
            print __call_method_0(__call_cls_builtin(str, "\n").__str__)
        else:
            if __call_method_1(__call_method_1(x.__mod__, __call_cls_builtin(int, 3)).__eq__, __call_cls_builtin(int, 0)):
                print __call_method_0(__call_cls_builtin(str, "X is a multiple of 3").__str__)
                print __call_method_0(__call_cls_builtin(str, "\n").__str__)
            else:
                if __call_method_1(__call_method_1(x.__mod__, __call_cls_builtin(int, 5)).__eq__, __call_cls_builtin(int, 0)):
                    print __call_method_0(__call_cls_builtin(str, "X is a multiple of 5").__str__)
                    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
                else:
                    print __call_method_0(__call_cls_builtin(str, "X is a prime number").__str__)
                    print __call_method_0(__call_cls_builtin(str, "\n").__str__)
                    if __call_method_1(x.__eq__, __call_cls_builtin(int, 1)):
                        print __call_method_0(__call_cls_builtin(str, "X is one").__str__)
                        print __call_method_0(__call_cls_builtin(str, "\n").__str__)
                    else:
                        print __call_method_0(x.__str__)
                        print __call_method_0(__call_cls_builtin(str, "\n").__str__)




        return None

    __call(test_if_elif_else_inner,__call_cls_builtin(int, 2))
    __call(test_if_elif_else_inner,__call_cls_builtin(int, 3))
    __call(test_if_elif_else_inner,__call_cls_builtin(int, 5))
    __call(test_if_elif_else_inner,__call_cls_builtin(int, 1))
    __call(test_if_elif_else_inner,__call_cls_builtin(int, 7))
    return None

__call(test_if)
__call(test_if_else)
__call(test_if_elif_else)