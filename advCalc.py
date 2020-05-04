#adv calc

import re

result=0
flag=True
print("Enter 'quit' to exit calculator.")
def advCalc():
    global flag
    global result
    string=""
    if result==0:
        string=input("Enter the equation: ")
    else:
        string=input(str(result))

    if(string=="quit"):
        flag=False
    else:
        string=re.sub('[a-zA-Z," ":;<>_\'\"]','',string)
        if result is 0:
            result=eval(string) 
        else:
            result=eval(str(result)+string)
        print("Result: ",result)


while(flag == True):
    advCalc()