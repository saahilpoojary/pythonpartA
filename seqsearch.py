from array import *
n=int(input("Enter the n value"))
arr=array('i',[])
for i in range(n):
    x=int(input(f"Enter the element {i+1}"))
    arr.append(x)
key=int(input("Enter the search element"))
for i in range(n):
    if arr[i]==key:
        print(f"Element found in location {i+1}")
        exit(0)
print("Element not found")
