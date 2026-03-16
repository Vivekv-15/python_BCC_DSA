def binary_search(list,target):
    low=0
    high=len(list)-1
    while low<=high:
        mid=(low+high)//2
        if list[mid]==target:
            return mid
        elif list[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1

list=[10,20,30,40]
target=40
index=binary_search(list,target)
print("element found at index: ",index)