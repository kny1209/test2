# 클래스 : 가방
# 객체 : 숄더백, 백팩, 클러치백, 핸드백
# 속성 : 재질, 색, 무게, 용량, 부피
# 기능 : 넣다, 꺼내다, 보호하다

class Bag:
    # 멤버변수
    # color = "black"
    # 메서드
    def __init__(self,name,color):
        self.name = name     
        self.color = color
        self.data = []

    def add(self,x):
        self.data.append(x)

    def addtwice(self,x):
        self.add(x)
        self.add(x)

shoulder = Bag("shoulder","black")
print(shoulder.color,shoulder.name)
shoulder.add("phone")
print(shoulder.data)
shoulder.addtwice("book")
print(shoulder.data)

print("--------------------")

carrier = Bag("carrier","white")
print(carrier.name,carrier.color)
carrier.add("passport")
print(carrier.data)
carrier.addtwice("money")
print(carrier.data)