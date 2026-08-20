num = int(input("Enter a 3-digit number: "))

original = num
total = 0

while num > 0:
    digit = num % 10
    total = total + digit ** 3
    num = num // 10

if total == original:
    print("It is an Armstrong number.")
else:
    print("It is not an Armstrong number.")