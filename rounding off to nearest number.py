def check(n):
    if n<38:
        return n
    elif n==38 or n==39:
        return 40
    elif n>38 and n%5==0:
        return n
    elif n>38 and (n%5)<4:
        if n%5==1:
            return n-1
        elif n%5==2:
            return n-2
        elif n%5==3:
            return n+2
        elif n>38 and n%5==4:
            return n+1
        elif n>38 and n%5<9 and n%5>4:
            if n%5==6:
                return n-1
            elif n%5==7:
                return n-2
            elif n%5==8:
                return n+2
    elif n>38 and n%5==9:
            return n+1

print(check(47))



