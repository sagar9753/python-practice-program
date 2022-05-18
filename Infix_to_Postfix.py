# from curses.panel import top_panel


# top=-1
# stack=[]


def convert(infix):
     global top
     postfix=[]
     for i in infix:
         if (i.is.digit()):
             postfix.append(i)
         elif (i=="("):
             stack.append(i)
             top+=1
         elif (i==")"):
             while(stack[top]!="("):
                 postfix.append(stack.pop())
                 top=top-1
             stack.pop()
             top=top-1
         else:
             if(top==-1):
                 stack.append()
                 top=+1
             elif(stack[top]="("):
                 stack.append()
                 top=top-1
                



x=input("Enter Expression")
y=convert(x)
print(y)
        
