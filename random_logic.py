import random
import time
inp1= int(input("Input for start random parameter: "))
inp2= int(input("Input for stop random parameter: "))
inp3 = int(input("Input for number of times to run the loop: "))
rndm = random.randint(inp1,inp2)
r1 = rndm

for i in range(10):
    print("This is a random number between ",inp1," and ",inp2,": ",r1)
    a = input("Type yes if you want to continue and No if you don't: ")
    if a.upper() == "YES":
        r1 = random.randint(inp1, inp2)
        continue
    elif a.upper()=="NO":
        a2 = input("Are you sure to stop the program? Type 'TAKE_ME_BACK(tmb)' to CONTINUE. Type 'ENTER' to TERMINATE: ")
        if a2.upper()=="TMB" or a2.upper()=="TAKE_ME_BACK":
            continue
        else:
            print("Stopped.")
            break
    else:
        print("Please type yes or no.")


