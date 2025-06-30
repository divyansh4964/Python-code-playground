#Find the N-th Digit from the Right

num = int(input("Enter number: "))
n = int(input("position from right: "))

i = 1
while i < n:
    num //= 10
    i += 1

digit = num % 10
print(digit)
