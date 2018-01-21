def used_bottles(a,n):
    i = a//n
    if a//n!=a/n:
        return (a//n)+1
    return a//n


a = int(input())
b = int(input())
if a == 0 or b == 0:
    print(0)
else:
    mina = 50 * (a-1)
    maxa = 50 * a
    minb = 70 * (b-1)
    maxb = 70 * b
    
    if mina>minb:
        final_min = mina
    else:
        final_min = minb
    if maxa<maxb:
        final_max = maxa
    else:
        final_max = maxb
    
    if final_min > final_max:
        print(-1)
    elif final_min == final_max:
        print(-1)
    else:
        bottles = []
        for i in range(final_min+1,final_max+1):
            if used_bottles(i,60) not in bottles:
                bottles.append(used_bottles(i,60))
        if len(bottles) == 1:
            print(bottles[0])
        else:
            for bottle in bottles:
                print(bottle,end = ' ')
