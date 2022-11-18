class A:
    pass

class B:
    pass

class C:
    pass

class D(A, B):
    pass

something = D()
print(isinstance(something, D))
print(issubclass(D, A))