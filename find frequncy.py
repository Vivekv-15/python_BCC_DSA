#find frequency of each element in list
num=[1,2,2,3,3,3,4,4,5,5,5,5]
dict={}
for i in num:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)
