from array import *
arr=array('i',[])
n=int(input("Enter the size of the array"))
for i in range(n):
    ele=int(input(f"Enter the element {i+1}: "))
    arr.append(ele)
    
print(arr)    
