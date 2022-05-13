

# --------   Without Function Use -------

n = int(input("Enter the total items "))
r = int(input("Enter the no of item to be arrange "))

# Calculate n factorial

fact_n = 1
for i in range(1, n+1):
    fact_n *= i


# Calculate n-r factorial
x = n-r
fact_x = 1
for i in range(1, x+1):
    fact_x *= i

P = fact_n/fact_x
print("Parmutation= ", P)

