num = 1234
rev_num = 0

while num != 0:
    digit = num % 10
    rev_num = rev_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(rev_num))
