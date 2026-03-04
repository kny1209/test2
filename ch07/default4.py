def persona(weight=170, height=51, age=24):
    print("default of func, wwight =",weight,"height =",height,"age =",age)

def personb(width=4, height=3):
    print("default of func, width =",width,"height =",height)

persona(168,55,22)
persona(168,55)
# persona()   
# personb()       # 기본값이 있음 데이터 값 설정 안 해도 된다

# 1. 모든 매개변수에 기본값 설정 가능
# 2. 부분 매개변수에 기본값 설정시 뒤에서부터 설정할 것
# 3. 기본값이 있더라도 인수를 설정 가능 (인수 우선 처리)
# 4. 인수 전달 시 앞에서부터 설정 가능

# 키워드 인수 : 이름을 지정해서 전달하는 인수
# 위치 인수 : 순서대로 전달하는 인수
persona(169,55,age=33)
# persona(268,age=34,weight=55) # 키워드 인수인 경우 순서 중요X
# persona(268,34,weight=55)     #위치 인수 순서 안 맞고 중복 -> 오류 발생

# 가변 위치 인자(*args) : 개수가 정해지지 않은 인자, tuple 형태
def total(*num):
    print(num)
total(1)
total(1,2)

# 가변 키워드 인자(**kwargs) : 이름 붙은 인수를 여러개 받음, dictionary 형태
def profile(**info):
    print(info)
profile(name="gildong",age=555,adress="hangyang")

# summation
def example(a, b=10, *args,**kwargs):
    print("a =",a,"b =",b,"args =",args,"kwargs =",kwargs)

example(1,2,3,4,100,y=200)