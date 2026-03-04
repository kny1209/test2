class Human:
    def __init__(self,age, name):
        self.age = age          #인스턴스 변수
        self.name = name

    def intro(self):            # 기능:자기소개
        print(str(self.age)+"살 "+self.name+"입니다")

#객체생성
kim = Human(29,"김상형")
lee = Human(45,"이승우")
#객체 접근(함수 호출)
kim.intro()
lee.intro()


na = 1      # 정수 객체 -> 클래스로 생성됨
na = int(10)    # int() -> 생성자 함수
print(type(na))
