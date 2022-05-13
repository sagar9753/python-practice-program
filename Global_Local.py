count = 1
def plus():
    global count 
    count += 1
def minus():
    global count
    count -= 1

    #  Error 
     #UnboundLocalError: local variable 'count' referenced before assignment
print("Count = ", count)

plus()
plus()
minus()
minus()
print("Count = ", count)
  



        