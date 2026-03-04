def persona(width, height):
    print("no default of func, width =",width,"height =",height)

def persona():
    print("no para func")   # 덮어쓴걸로 보면 된다

def personb(width=4, height=3):
    print("default of func, width =",width,"height =",height)

# persona(10,20)
persona()   # 인수와 매겨변수가 대응이 되지 않음 -> 오류발생
personb()       # 기본값이 있음 데이터 값 설정 안 해도 된다
# personb(13,78)  # 기본 데이터값보다 우선수위가 높다

