class A:
    def __init__(self,a:int):
        self.a = a
    
    def square(self, a):
        return self.a * self.a
    
class B(A):
    def __init__(self,a:int):
        self.a = a+2
        super().__init__(self.a)

b=B(2)
print(b.square(10))