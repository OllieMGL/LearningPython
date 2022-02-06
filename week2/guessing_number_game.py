import random 
import time 

nums = list(range(1, 100))

retry = "y"

time.sleep(0.25)
print("\nPlease guess a randomly generated number between 1 and 100!")
time.sleep(1)
while retry == "y":
    counter = 0
    guessnumber = random.choice(nums)
    number = int(input("\nEnter your guess guess a number: "))

    while number != guessnumber:
        time.sleep(0.25)
        print("Try agin!")

        if number > guessnumber and number > 100:
             time.sleep(0.5)
             print("You went above 100! It aint gonna be that dummo.")

        elif number > guessnumber:
             time.sleep(0.5)
             print("Your number is too high,")

        elif number < guessnumber:
             time.sleep(0.5)
             print("Your number is too low,")

        time.sleep(0.8)
        number = int(input("\nPlease guess a number: "))
        counter = counter + 1 

    print("Correct!")
    counter = counter + 1 
    print("You guessed the correct number in " + str(counter) + " attempts", end= ' ', flush=True)

    retry = input("Would you like to play again? (y/n): ")

    if retry == "y":
        print("please wait whilst we generate a new number")
        time.sleep(0.25)
        print(".", end= ' ', flush=True)
        time.sleep(0.25)
        print(".", end= ' ', flush=True)
        time.sleep(0.25) 
        print(".",  end= ' ', flush=True)
        time.sleep(0.25)
        input("\nplease press enter to continue...")
     
    else:
        print("Thank you for playing!")
        exit()
        
    

