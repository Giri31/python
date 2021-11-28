n=int(input())
val=1
val2=n-1
for i in range(1,n+1):
    print(' '*val2 + '#'*val)
    val+=1
    val2-=1
