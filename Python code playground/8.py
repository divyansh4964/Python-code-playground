#Find First Digit of a Number

n = int(input("Enter a number:"))

while n >= 10:
    n = n // 10

print(n)
