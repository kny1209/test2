# define class
class Cvalue:
    def __init__(self):
        self.lista = []
    def add(self,num):
        self.lista.append(num)
    def delete(self,num):
        self.lista.remove(num)
    def add2(self, i, num):
        self.lista.insert(i,num)
    def fprint(self):
        print(self.lista)

# define func
def plus(a,b):
    c = a + b
    return c

# create obj


p1 = Cvalue()
p1.add(1)
p1.add(2)
p1.add(3)
p1.fprint()
p1.delete(2)
p1.fprint()
p1.add2(0,18)
p1.fprint()

print(__name__)     # main module