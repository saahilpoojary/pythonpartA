def fib(n):
    if n<=1:
        return n
    else:
        return(fib(n-1)+fib(n-2))


n=int(input("Enter the value of n"))
for i in range(n):
    print(f"{fib(i)} ",end="")
