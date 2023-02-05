def fibonacci():
    index = int(input("Insert the index: "))
    prev = 0
    next = 1
    i = 0
    while i <= index:
        sum = next + prev
        prev = next
        next = sum
        i+=1
    print(prev)

fibonacci()