# 3. Check for a Special 2-Digit Number
#Example: 59 -> 5*9 + 5+9 = 45 + 14 = 59 -> True

n = 59

tens = n // 10

ones = n % 10

if tens* ones + tens + ones == n:
    print("True")
else:
    print("False")
