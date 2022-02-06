class Monster:
   #A monster has health and a type
   
    #Constructor
    def __init__(self, monster_health, monster_type):
        self.health = monster_health
        self.m_type = monster_type
        
    def tostring(self):
        return f"health is {self.health} and type is {self.m_type} "
        
    def take_damage(self, damage):
        self.health = self.health - damage
        
        
        
monster1 = Monster(10, "water")

monster2 = Monster(20, "fire")

monster3 = Monster(25, "grass")

#print(monster1.tostring())
#print(monster2.tostring())
#print(monster3.tostring())


#monster1.take_damage(10)
#print(monster1.tostring())

monsters = [monster1, monster2, monster3]

while len(monsters) > 0:
    
    
    #goes through the list and completes tostring - checks health
    for monster in monsters:
        print(monster.tostring())
    
    
    target = int(input("which monster do you want to attack? "))
    
    monsters[target].take_damage(10)
    
    #goes through the list and checks if monsters health is below 0
    #if it is it removes it from the list
    for monster in monsters:
        if monster.health < 1:
            monsters.remove(monster)

            
print("You have defeated all the monster!")           
        

    
    
    