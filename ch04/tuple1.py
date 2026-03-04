# clovers = ('clover1','clover2', 'clover3')
# print(clovers[1])
# print(type(clovers))

my_tuple = ()
print(my_tuple)

my_tuple = (1,2,True,'hi')
print(my_tuple)

my_tuple = 1,2,True,'hi'
print(my_tuple)
print(type(my_tuple),"\n----------------------")

# my_tuple[3] = False 수정불가

my_int = (1)
print(type(my_int))
print(my_int)

my_int = 1,    #() 생략 -> tuple 
print(type(my_int))
print(my_int)

t1 = (1,)
t2 = (2,)
print(t2 + t1)
print(type(t1[0]), "\n----------------------")

a = (1,2,3)
print(type(a))
b = list(a)
print(b, type(b))
b.insert(0,0)
print(b)