num=int(input())

sum=0
count=0
x=0
y=count/2
while(sum<num):
    #sum=14
    count+=1
    sum+=count
sum1=sum-count
#sum1=10
1,3,6,10,15
count2=0
while(sum1<num):
    if((count)%2==0):
        y=count-count2
        count2+=1
        x+=1
        sum1+=1
    elif((count)%2==1):
        y+=1
        x=count-count2
        count2+=1
        sum1+=1
    else:
        print("error")
y=int(y)
print("{0}/{1}".format(x,y))

