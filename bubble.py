from array import *
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr=array('i',[])
for i in range(5):
    x=int(input(f"Enter the element {i}"))
    arr.append(x)
bubble_sort(arr)
print("Sorted array:", arr)
