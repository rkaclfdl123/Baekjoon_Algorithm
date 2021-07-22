num=int(input())
A=[]
B=[]
C=[]
for i in range(num):
    a,b,c=list(map(int,input().split()))
    A.append(a)
    B.append(b)
    C.append(c)
#A 층수
#B 방수
#C 몇번째손님

for i in range(num):
    C1=C[i]
    A1=A[i]
    count1=0
    count2=0
    count3=0
    count1=C1%A1
    if(count1==0):
        count1=A1
        count2=C1//A1
    elif(count1!=0):
        count2=C1//A1+1
    else:
        print("error")
    print(int(count1)*100+ int(count2))
        