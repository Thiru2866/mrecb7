a=[2,0,4,5,9,7]
first=second=a[0]
for i in range(len(a)):
    if(a[i]>first):
        first=a[i]
    elif(a[i]>second and a[i]<first):
        second=a[i]
        print(second)