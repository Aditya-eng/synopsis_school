import random
inp1 = input("Let's start the game Enter any Key: ")
rndm = random.randint(1, 6)
r1=0

def email_slicer():
    for i in range(10):
        print("You're really lucky. You got the chance to slice your email!! ")
        email = input("Input your EMAIL ID to slice it!: ").strip()
        if "@" not in email:
            print("@ is not there.")
        username = email[:email.index('@')]
        domain = email[email.index('@') + 1:]
        print("Your username is ", username, " & domain is ", domain)
        email1 = input("If you want to slice another email press 'cont' ,if not type 'STOP': ")
        if email1 == "cont":
            continue
        else:
            print("STOPPED SUCCESSFULLY!(you typed STOP or something else)")
            break

def guess_the_word():
    print("OMG! It's GUESS THE WORD.")

    # library that we use in order to choose
    # on random words from a list of words

    name = input("What is your name? ")
    # Here the user is asked to enter the name first
    print("Here's a Hint for you, the names resemble cats and destinations.Enjoy!")
    print("Good Luck !", name)

    words = ['jaguar', 'panther', 'tiger', 'leopard',
             'lion', 'mavericks', 'yosemite', 'elcaptain',
             'sierra', 'mojave', 'catalina', 'bigsur','monetery']

    # Function will choose one random
    # word from this list of words
    word = random.choice(words)

    print("Guess the characters")

    guesses = ''

    # any number of turns can be used here
    turns = 12

    while turns > 0:

        # counts the number of times a user fails
        failed = 0

        # all characters from the input
        # word taking one at a time.
        for char in word:

            char1 = len(char)
            if (char in guesses) and (char1 ==1):
                print(char[0])

            else:
                print("_")

                # for every failure 1 will be
                # incremented in failure
                failed += 1

        if failed == 0:
            # user will win the game if failure is 0
            # and 'You Win' will be given as output
            print("You Win")

            # this print the correct word
            print("The word is: ", word)
            break

        # if user has input the wrong alphabet then
        # it will ask user to enter another alphabet
        guess = input("guess a character:")

        guesses += guess

        # check input with the character in word
        if guess not in word:

            turns -= 1

            # if the character doesn’t match the word
            print("Wrong")
            print("You have", + turns, 'more guesses')

            if turns == 0:
                print("You Loose")

def countdown_calculator():
    # for i in range(10):
    #     print("You're really lucky. You got the chance to slice your email!! ")
    #     email = input("Input your EMAIL ID to slice it!: ").strip()
    #     if "@" not in email:
    #         print("NOT")
    #         break
    #     username = email[:email.index('@')]
    #     domain = email[email.index('@') + 1:]
    #     print("Your username is ", username, " & domain is ", domain)
    #     email1 = input("If you want to slice another email press 'cont' ,if not type 'STOP': ")
    #     if email1 == "cont":
    #         continue
    #     else:
    #         print("STOPPED SUCCESSFULLY!(you typed STOP or something else)")
    #         break
    print("Welcome to Countdown Calculator!!!")
    print("Enter the starting date and eding date to find the period between them.")

    a, b, c = [int(x) for x in input("Enter the starting date:").split()]
    print("Date is ", a, b, c)

    d, e, f = [int(x) for x in input("Enter the starting date:").split()]
    print("Date is ", d, e, f)

    year = f - c
    month = e - b
    day = d - a

    var1 = 1
    var2 = 0

    if month < 0:
        var1 = var1 * 12 - abs(month)
        year -= 1
        month = var1
        print(day, "Day", month, "-month", year, "-Year")
        if day < 0:
            var2 = var2 * 30 - abs(day)
            day = var2
            month -= 1
            print(day, "Day", month, "-month", year, "-Year")
        else:
            print(day, "Day", month, "-month", year, "-Year")
    else:
        print(day, "Day", month, "-month", year, "-Year")

def fibonacci_checker():
    for i in range(10):
        print()
        print("Welcome to Find out Fibonacci!!")
        print("You'll have to give a number and the program will check if its in fibonacci.")
        # A number is Fibonacci if and only if one or both of (5*n^2 + 4) or (5*n^2 – 4) is a perfect square
        fib1 = int(input("Enter the number (0 for stopping): "))
        fib3 = fib1 * fib1 * 5 + 4
        fib5 = fib1 * fib1 * 5 - 4
        fib4 = fib5 ** 0.5
        # fib2 = math.isqrt(fib3)
        fib2 = fib3 ** 0.5
        # print(fib3, fib2)
        # print(fib2.is_integer())
        if (fib2).is_integer() == True or (fib4).is_integer() == True:
            print(fib1, "is a fibonacci number.")
            # print(fib1, fib2, fib3)

        if fib1 == 0:
            print("STOPPED.")
            break
        elif (fib2).is_integer() == False or (fib4).is_integer() == False:
            print("NOT FIBONACCI")

def rock_paper_scissors():
    rpslist = ["R", "P", "S"]
    print("Welcome to rock-paper-scissors !!!")
    rps4 = int(input("Enter the number of times you want to play: "))
    i=0
    if type(rps4) == int:
        while i != rps4:
            i += 1
            print("R for Rock, P for Paper and S for Scissors, STOP for quitting.")
            rps3 = input("Enter when you're ready: ")
            rps1 = random.choice(rpslist)
            if rps3.upper() == rps1:
                print(rps3.upper())
                print("Uh'oh try again")
                rps1 = random.choice(rpslist)
                continue
            elif (rps3.upper() == "R" and rps1 == "P") or (rps3.upper() == "P" and rps1 == "S") or (
                    rps3.upper() == "S" and rps1 == "R"):
                print("You LOSE, it was ", rps1)
                rps1 = random.choice(rpslist)
                print()
            elif (rps3.upper() == "R" and rps1 == "S") or (rps3.upper() == "P" and rps1 == "R") or (
                    rps3.upper() == "S" and rps1 == "P"):
                print("You WIN, it was ", rps1)
                rps1 = random.choice(rpslist)
                print()
            elif rps3.upper() == "STOP" or rps3 == "QUIT":
                print('STOPPED SUCCESSFULY')
                break

            else:
                print("Type ONLY R,P,S")
                print()
    else:
        print("NOT A NUMBER")



def leap_it():

    for i in range(10):
        li = input("Enter the year(0 for stop): ")
        if len(li) <= 4:
            if li % 4 == 0:
                if li % 100 == 0:
                    if li % 400 == 0:
                        print(li, " is a Leap Year.!")
                    else:
                        print(li, " is not a Leap Year.")
                else:
                    print(li, " is a leap year.")
            elif li == 0:
                print("STOPPED SUCCESSFULLY")
                break
            else:
                print(li, " is not a Leap Year.")





###### FINAL CODE ################

if type(inp1.upper()) == type(str()) or type(inp1.upper()) == type(int()):
        rndm = random.randint(1, 6)
        r1 = rndm
        print("The dice has been rolled!")
        print("And the number is ", r1)
        print()

        if r1 == 1:
            email_slicer()

        elif r1==7 :
            guess_the_word()

        elif r1==7:
            fibonacci_checker()

        elif r1==7 :
            rock_paper_scissors()

        elif r1==7:
            leap_it()
            print()

        else:
            email_slicer()
            # countdown_calculator()


