'''
# 클래스 정의
class 클래스명:
    # 멤버변수 
    변수명 = 데이터값 
    # 멤버함수 (=메서드)
    def 함수명(self, 매개변수, ...):
        # 멤버변수
        self.변수명 = 데이터값
        return 반환값

# 객체 생성 (생성자함수 활용)
객체변수명 = 클래스명()
# 객체 접근
객체변수명.변수명
객체변수명.함수명(인수1, ...)
'''

# 빈 클래스 작성
# class 클래스명:
#     pass

class Pizzaclass:
    def order(self):
        print("order")
        self.kind = 10

combo = Pizzaclass()
combo.order()           # 멤버 함수 호출 
print(combo.kind)       # 멤버 변수 접근