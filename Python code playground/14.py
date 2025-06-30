# Check if Digits Are in Increasing Order

n = int(input("Enter a number:"))
increasing = True
last_digit = -1

while n > 0:
    digit = n % 10
    if last_digit != -1 and digit >= last_digit:
        increasing = False
    last_digit = digit
    n //= 10

if increasing :
    print("Yes")
else:
    print("No")
