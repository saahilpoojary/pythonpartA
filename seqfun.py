from array import *

def seqsearch(arr,key,n):
    for i in range(n):
        
        if arr[i]==key:
            return 1
    return 0
            
n=int(input("Enter the n value"))
arr=array('i',[])
for i in range(n):
    x=int(input(f"Enter the element {i+1}"))
    arr.append(x)
key=int(input("Enter the search element"))
found=seqsearch(arr,key,n)
if(found>=1):
    print("Element found")
else:
    print("Element not found")
