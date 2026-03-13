# remove duplicates in list
num=[2,3,4,4,5,5,6,6,7,2]
rem=[]
for i in num:
    if i not in rem:
        rem.append(i)
print("Actual list:",num)
print("After removing:",rem) 