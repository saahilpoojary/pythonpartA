from array import *
arr=array('i',[])
n=int(input("Enter the size of the array"))
for i in range(n):
    ele=int(input(f"Enter the element {i+1}: "))
    arr.append(ele)
print(arr)
d=0
while(d!="no"):
 d=str(input("Do you want to access the elements idividually, type yes no"))
 if(d=="yes"):
  acc=int(input("Enter the index of element you want to access"))   
  print(arr[acc-1])
 if(d=="no"):
    print("Thank you") 
