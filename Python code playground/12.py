# Print All Prime Numbers from 1 to N

n = int(input("Enter a number: "))
m = 2

while m <= n:
    i = 2
    while i < m:
        if m % i == 0:
            break
        i += 1
    if i == m :
        print(m, end=" ")
    m += 1
