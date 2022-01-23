compunum = 50

number = int(input("please guess a number "))

while number != compunum :
    print("try again!")

    if number > compunum :
        print("your number is too low, guess higher")

    elif number < compunum :
        print("your number is too high, guess lower ")

    number = int(input("please guess a number "))

print("nice")