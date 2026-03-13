# find all pairs in a list whose sum eql to target
num=[2,4,3,5,7,8,9]
target=10
rem=[]
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if(num[i]+num[j]==target):
            rem.append((num[i],num[j]))
print("pair is ",rem)      
