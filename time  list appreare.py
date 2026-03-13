# count how many times each element appears in list
num=[1,2,2,3,3,3,4,4,5,5,5,5]
dict={} 
for i in num:
    dict[i]=dict.get(i,0)+1
print(dict)  
# 2nd approch
dict2={}
for i in num:
    if i in dict2:
        dict2[i]+=1
    else:
        dict2[i]=1
print(dict2)    