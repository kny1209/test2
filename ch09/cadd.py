class Cadd:
    def fadd(self,a,b):
        self.a = a
        self.b = b
        self.hap = self.a + self.b

obj = Cadd()
obj.fadd(10,20)
print("a :",obj.a)
print("b :",obj.b)
print("hap :",obj.hap)