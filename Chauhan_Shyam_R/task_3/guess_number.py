import random

class guess_number:
    def __init__(self):
        self.temp = 0
        self.range = 50

    def number_generator(self):
        return random.randint(0,self.range+1)


    def user_guess(self,num):
        print(num)
        print("Guess the number between 0 to 50(inclusive)")
        print("you will get 5 tries")
        for i in range(0,5):
            self.temp = int(input("Enter Your guess : "))
            if(self.temp > self.range):
                print("Guess in between given range :/")
            else:
                if(self.temp == num):
                    print("Nice, Your guess is correct !")
                    exit(0)
                else:
                    print("Wrong guess")
        print("Out of tries !")


def main():
    print("Welcome to number guessing game !")
    gs = guess_number()
    num = gs.number_generator()
    gs.user_guess(num)

if __name__ == '__main__':
    main()