#Create a Pattern Without Using Arrays
#1
# 12
# 123
# 1234

n = int(input("Enter a number: "))

i = 1
while i <= n:
    j = 1
    while j <= i:
        print(j, end="")
        j += 1
    print()
    i += 1

