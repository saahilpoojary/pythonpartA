num1=int(input("Enter the number 1 "))
num2=int(input("Enter the number 2 "))
if(num1>num2):
    temp=num1
    num1=num2
    num2=temp 
for i in range(1,num2+1): #num2+1 because for loop traverses till num2-1 only
    if num1%i==0 and num2%i==0:
        ans=i
print(f"The GCD of {num1} and {num2} is {ans}")
