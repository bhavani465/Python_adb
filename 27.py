#27. Take some single digit numbers from the user and findout min, maximum, sum, average

max,sum=0,0
a=input("enter single digit numbers: ")
a=a.split()
min=int(a[0])
for i in range(len(a)):
    if len(a[i])>1:
        print("please enter single digit numbers")
        exit(0)
    a[i]=int(a[i])
    if a[i]>max:
        max=a[i]
    if a[i]<min:
        min=a[i]
    sum=sum+a[i]
print("biggest number is: ",max)
print("min number is: ",min)
print("sum of numbers: ",sum)
print("average of numbers:",(sum/len(a)))