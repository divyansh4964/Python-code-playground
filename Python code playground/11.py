#Print Number Pyramid with Powers

n = int(input("Enter a number:"))
i = 1

while i <= n:
    j = 1
    k = 1
    while j <= i:
        print(k, end=" ")
        k = k * 2  
        j += 1
    print()
    i += 1
