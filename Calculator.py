class myCalculator():
    def firstAsking(self):
        print("Hello This it's a Calculator-Project")
        print("""
        ***********
        | | | | | |
        ***********
              """)
    def operation(self):
        while True:
            try:
                ops = input("Enter the operation (+, *, -, /) or 'exit' the quit:")
                if ops == "exit":
                    print("Exiting  the calculator")
                    break
                if ops in ["+", "*", "-", "/"]:
                    num1 = float(int(input(" --- Enter You 1st Number --- ")))
                    num2 = float(int(input(" --- Enter You 2st Number --- ")))
                if ops == "+":
                    result = num1 + num2
                    print(f"You result it's { num1 } + { num2 } = { result }")
                elif ops == "*":
                    result = num1 * num2 
                    print(f"You result it's { num1 } * { num2 } = { result }")
                elif ops == "-":
                    result = num1 - num2
                    print(f"You result it's { num1 } - { num2 } = { result }")
                elif ops == "/":
                    if ops != 0:
                        result = num1 / num2
                        print(f"You result it's { num1 } / { num2 } = { result }")
                    else:   
                        print("Zero division it's not allowed.")
                else:
                    print("You enter a wrong operation")
            except ValueError:
                print("Value Error :  Please interic values for the number")
                    
                
            
                    

calculator = myCalculator()
calculator.firstAsking()
calculator.operation()