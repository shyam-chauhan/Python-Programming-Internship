class Calc:

    # def __init__(self):
    #     self.num1 = num1
    #     self.num2 = num2

    def addition(self,num1,num2):
        return num1 + num2
    
    def subtraction(self,num1,num2):
        return num1 - num2

    def multiplication(self,num1,num2):
        return num1 * num2
    
    def division(self,num1,num2):
        if(num2 == 0):
            return "can not divide by Zero"
        else:
            return num1/num2

def main():
    choice = 1
    calc = Calc()
    while True:
        choice  = int(input("Please choose from following \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Exit \nEnter your choice : "))
        if (choice != 5):
            num1 = int(input("Enter first number : "))
            num2 = int(input("Enter Second number : "))
        else:
            pass
        if(choice == 1):
            temp = calc.addition(num1,num2)
            print("Addition is : ",temp)
        elif(choice == 2):
            temp = calc.subtraction(num1,num2)
            print("Subtraction is : ",temp)
        elif(choice == 3):
            temp = calc.multiplication(num1,num2)
            print("Multiplication is : ",temp)
        elif(choice == 4):
            temp = calc.division(num1,num2)
            print("Division is : ",temp)
        elif(choice == 5):
            exit(0)
        else:
            print("Wrong choice !")

if __name__ == '__main__':
    main()
