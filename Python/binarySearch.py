import math

def binarySearch(arr, num):
    min = 0
    max = len(arr)
    mid = 0
    i = 1
    
    while i < math.floor(len(arr)/2):
        mid = math.floor((min + max) / 2)
        if arr[mid] == num:
            return(f"The loop ran {i} times and the number {num} is at the index {mid}")
        elif arr[mid] > num:
            max = mid-1
        elif arr[mid] < num:
            min = mid+1
        i=i+1

    return "Coudn't find the given number in the array..."

print(binarySearch([1,2,3,4,5,6,7,8,9,10], 1))