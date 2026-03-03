import mex1
import mex1 as m1   # 별칭(alias) 사용

# mex1 -> 하위 모듈 동작

print("--------------------")
p2 = mex1.Cvalue()
print(p2.lista)
p2.add(11)
p2.add(21)
p2.add(31)
p2.fprint()
p2.delete(11)
p2.fprint()
v = mex1.plus(19,20)
print(v)
p2.add2(0,83)
p2.fprint()
print("--------------------")
# mex1.py 변수 활용
print(mex1.p1.lista)
mex1.p1.add(4)
mex1.p1.fprint()

print(__name__)     # main module