available_commands=tuple(["+","-","*","/"])
#-------------------------------------------#
def sum(n1,n2):
    return n1+n2
#-------------------------------------------#
def minus(n1,n2):
    return n1-n2
#-------------------------------------------#
def multiply(n1,n2):
    return n1*n2
#-------------------------------------------#
def division(n1,n2):
    return n1/n2
#-------------------------------------------#
def run():
    while True:
        command=input("please use one of the following symbols(+,-,*,/) or type \"exit\" to exit: ")
        if command=="exit":
            break
        if command not in available_commands:
            continue
        num1=num2=None
        while True:
            try:
                num1=float(input("Enter your first number: "))
                break
            except ValueError:
                print("Invalid input\n")
                continue 
        while True:
            try:
                num2=float(input("Enter your second number: "))
                if num2==0 and command=="/":
                    print('can\'t divide by zero\n')
                    continue
                break
            except ValueError:
                print("Invalid input\n")
                continue           
        if command =="+":
            print(sum(num1,num2))   
        elif command =="-":
            print(minus(num1,num2))
        elif command =="*":
            print(multiply(num1,num2))
        else:
            print(division(num1,num2))    
  