ca = [21,10,11,15,13]

for sb in range(0,4,1):
    mina = ca[sb]
    minx = sb

    for sa in range(sb+1,5,1):
        if mina > ca[sa]:
            mina = ca[sa]
            minx = sa

    temp = ca[sb]
    ca[sb] = ca[minx]
    ca[minx] = temp
    print(ca)

