bulbasaur = ["small", "green"]
psyduck = ["small", "yellow"]
cubone = ["small", "brown"]
zapdos = ["big", "yellow"]

def isLegendary(pokemon):
    if (pokemon[0] == "big" and pokemon[1]== "yellow"):
        print("Legendary", end=": ")
 


def identify(pokemon):
    isLegendary(pokemon)
    if (pokemon[0] == "big"):
        return("run away")

    elif(pokemon[1] == "brown"):
        return("run away")

    else:
        return("fight")
        
    

bulbasaur_result = identify(bulbasaur)
print(bulbasaur_result)
print(identify(psyduck))
print(identify(cubone))
print(identify(zapdos))

