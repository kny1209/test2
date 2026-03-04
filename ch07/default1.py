'''
def 함수명(매개변수1=기본값1,매개변수2=기본값2,...):
    코드블록
    return 반환값

함수명(인수1,인수2,...)
'''

def persona(width, height):
    print("no default of func, width =",width,"height =",height)

def personb(width=4, height=3):
    print("default of func, width =",width,"height =",height)

persona(10,20)
persona(6,12)   # 인수와 매겨변수가 대응이 되지 않음 -> 오류발생
personb()       # 기본값이 있음 데이터 값 설정 안 해도 된다
personb(13,78)  # 기본 데이터값보다 우선수위가 높다

