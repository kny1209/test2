from mex1 import plus
from mex1 import plus as m1_plus #별칭
from mex1 import Cvalue
from mex1 import p1

print('--------------------')
value = plus(10,20)
print(value)

print('--------------------')
p3 = Cvalue()
p3.add("apple")
p3.add("pear")
print(p3.lista)

print('--------------------')
p1.add(32)
print(p1.lista)

print(__name__)
# 파이썬 부분 임포트시 특정 클래스, 함수, 변수를 명시하는 이유
# 1. 코드 간결화 (가독성)
# 2. 네임스페이스 충돌 방지
# 3. 기능 사용의 명확성
# 단, 실행 성능 차이는 거의 없음