guessnumber = 68 
number = int(input("Please guess a number"))

while number != guessnumber:
    print("Try agin!")
    
    if number > guessnumber:
        print("your number is too high")
    
    elif number < guessnumber:
        print("your number is too low")
        
    
    number = int(input("Please guess a number"))
    
print("correct")