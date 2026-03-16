def linearsearch(list,target):
    for i in range(len(list)):
        if list[i]==target:
            return i
    return -1

list=[10,20,30,40]
target=40
index=linearsearch(list,target)
print("element found at index: ",index)