num = int(input("Enter a 3-digit number: "))

if 100 <= num <= 999:
    hundred = num // 100
    ten = (num // 10) % 10
    one = num % 10

    if hundred**3 + ten**3 + one**3 == num:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")
else:
    print("Please enter a 3-digit number.:(")