def persona(width=11, height=41):
    print("no default of func, width =",width,"height =",height)

def personb(width=4, height=3):
    print("default of func, width =",width,"height =",height)

persona(10,20)
persona()   
personb()       # 기본값이 있음 데이터 값 설정 안 해도 된다

