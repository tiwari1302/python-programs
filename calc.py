#basic calc
def add(num1, num2):
    return num1+num2
def sub(num1, num2):
    return num1-num2
def mult (num1, num2):
    return num1*num2
def div(num1, num2):
    return num1/num2
x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))
print("1. Add\n2. Sub\n3. Mult\n4. Div")
choice=int(input("Enter your choice: "))
if choice==1:
    print(x,"+",y,"=",add(x,y))
elif choice==2:
    print(x,"-",y,"=",sub(x,y))
elif choice==3:
    print(x,"*",y,"=",mult(x,y))
elif choice==4:
    print(x,"/",y,"=",div(x,y))
else:
    print("Fooled!")
