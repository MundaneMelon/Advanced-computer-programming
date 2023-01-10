class ClassA:
    pass

class ClassB(ClassA):
    pass

class ClassC:
    pass

class ClassD(ClassC):
    pass

object_a = ClassA()
object_b = ClassB()
object_c = ClassC()
object_d = ClassD()

print(isinstance(object_b, ClassA))
print(isinstance(object_d, ClassC))
print(isinstance(object_b, ClassC))
print(isinstance(object_b, ClassA))