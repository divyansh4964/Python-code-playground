# Armstrong Number Checker (3-digit)
# Input: 153 -> 1³ + 5³ + 3³ = 153


num = int(input("Enter a 3-digit number: "))
actual_number = num
cubic_sum = 0

while num > 0:
    digit = num % 10
    cubic_sum += digit * digit * digit
    num = num // 10

if cubic_sum == actual_number:
    print("Armstrong")
else:
    print("Not Armstrong")
