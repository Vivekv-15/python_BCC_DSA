#constant time 
list=[10,20,30,40,50]
print(list[1])

for i in list:
    print(i)
    
#0(n) = binary search 
array1=[1,2,3,4,5,6,7,8,9]
copy_arr=array1[:]
print(copy_arr)

#0(n2) =shorting
list1=[1,2,3,4]
for i in list1:
    for j in list1:
        print(i,j)


list3=[9,7,5,4,6,3,2,1]
print(sorted(list3))
# O(2n)==> recursive approch  fibonacci