class A:
    def f(self):
        return 1
class B:
    def f(self):
        return "str"
class C(A, B):
    pass

x = C().f()


class D:
    def f(self, x , y=2) :
        x = 1
        return x
class E(D):
    def f(self, x,y=2,z=3):
        return x
    
def foo(a: D):
    x = a.f(1)
    x = x +10

foo_out = foo(D())