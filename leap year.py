a=int(input("Enter a year : "))

if(a%4==0 and a%100 or a%400==0):
    print("year is leap year")
else:
    print("Year is not leap year")
