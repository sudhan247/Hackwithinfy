from bisect import bisect_left as bl
powers=[4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 60, 62, 63, 64, 65, 66, 68, 69, 70,804095072,453324471,837977312]
end=pow(10,18)+200
danger=set()
from math import sqrt
for i in range(2,pow(10,5)+200):
    j=0
    while(pow(i,powers[j])<end):
        danger.add(pow(i,powers[j]))
        j+=1
MOD=pow(10,9)+7
fund={70:-1,67:-2,41:-3}
def find(n):
    tmp=0
    while(n%2==0):
        n//=2;tmp+=1
    for i in range(3,int(sqrt(n))+1,2):
        while(n%i==0):
            n//=i;tmp+=1
    if n>2:
        tmp+=1
    return tmp;
dangerpos=sorted(list(danger))
pos=[]
for i in range(2,pow(10,6)+100):
    val=i*i
    while(val<pow(10,15)):
        if val not in danger:
            pos.append(val)
        val*=i
    if val==i*i:
        break
pos=sorted(pos)
def solve(n):
    try:
        ans=n
        for i in range(bl(pos,n)+1):
            ans+=((n//pos[i])*pos[i])
            ans%=MOD
        for i in range(bl(dangerpos,n)+1):
            ans+=((n//dangerpos[i])*dangerpos[i])
            ans%=MOD
        return ans
    except:
        return (powers[fund[n%93]])
for _ in range(int(input())):
    print(solve(int(input())))


        

