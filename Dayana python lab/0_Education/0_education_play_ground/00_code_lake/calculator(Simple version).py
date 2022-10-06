
# Get the first input number
def get_number1():
    num1 = input("please inter number1:")

    try: 
        num1_f = float(num1)
        return num1_f
    except:
        print("please enter a number!!!")
        return get_number1() #recursive function

# Get operator between two numbers
def get_operator():
    op = input("please inter '*' or '/' or '+' or '-' :") # op stands for operator

    if op.upper() == '*' or op.upper() == '/' or op.upper() == '+' or op.upper() == '-':
        return op.upper()
    else:
        print("input is valid")
        return get_operator() #recursive function

#Get the second number
def get_number2():
    num2 = input("please inter number2:")

    try: 
        num2_f = float(num2)
        return num2_f
    except:
        print("please enter a number!!!")
        return get_number2()#recursive function


def Definition_operations(num1, op, num2):
    match op:
        case "*":
          return  print(num1, "*", num2 ,"=", num1*num2) # Definition of multiplication operation
        case "/":
          return  print(num1, "/", num2 ,"=", num1/num2) # Define the division operation
        case "+":
          return  print(num1, "+", num2 ,"=", num1+num2) # Definition of addition operation
        case "-":
          return  print(num1, "-", num2 ,"=", num1-num2) # Definition of minus operation
        



if __name__ == "__main__":
 
 num1 = get_number1()
 op = get_operator()
 num2 = get_number2()
 
 Definition_operations(num1, op, num2)
 
input("press any key to exit...")




