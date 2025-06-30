# Check if Number is a Harshad Number

n = int(input("Enter a number:"))
x = n
sum_digits = 0

while x > 0:
    sum_digits += x % 10
    x //= 10

if n % sum_digits == 0:
    print("Yes")
else:
    print("No")
