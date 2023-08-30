
import random

beatemup = """
  ____             _      _                   _    _       
 |  _ \           | |    ( )                 | |  | |      
 | |_) | ___  __ _| |_   |/  ___ _ __ ___    | |  | |_ __  
 |  _ < / _ \/ _` | __|     / _ \ '_ ` _ \   | |  | | '_ \ 
 | |_) |  __/ (_| | |_     |  __/ | | | | |  | |__| | |_) |
 |____/ \___|\__,_|\__|     \___|_| |_| |_|   \____/| .__/ 
                                                    | |    
                                                    |_|    
"""

print(beatemup)


# Create Enemy class
class Enemy:
  def __init__(self, name, level, damage, special_act, health=0):
    self.name = name
    self.level = level
    self.health = level * 5
    self.damage = damage
    self.special_act = special_act

  # Describe the enemy
  def __repr__(self):
    description = "This level {level} enemy is called {name}. They have {health} points of health and deal {damage} damage. Their special action is {special_act}.".format(level = self.level, name = self.name, health = self.health, damage = self.damage, special_act = self.special_act)
    return description

  # Slap the player
  def slap(self, player):
    if self.health <= 0 :
      print("{name1} can't slap {name2}; they're knocked out!".format(name1=self.name, name2=player.name))
    elif player.health <= 0 :
      print("{name1} slaps {name2}...which is super fucked up, because she's passed out...".format(name1=self.name, name2=player.name))
    else :
      print("{name1} slaps {name2}. It doesn't hurt her, but it's super rude.".format(name1=self.name, name2=player.name))

  # Punch the player
  def punch(self, player):
    if self.health <= 0 :
      print("{name} can't attack; they're knocked out!".format(name=self.name))
    elif player.health <= 0 :
      print("{name1} can't attack; {name2} is knocked out!".format(name1=self.name, name2=player.name))
    else :
      player.health -= self.damage
      if player.health <= 0 :
        print("{name1} punches {name2}.".format(name1=self.name, name2=player.name))
        print("{name2} has been knocked out!".format(name2=player.name))
        print("You lose!")
      else:
        print("{name1} punches {name2}. {name2} takes {damage} damage!".format(name1=self.name, name2=player.name, damage=int(self.damage)))

  # Kick the player
  def kick(self, player):
    if self.health <= 0 :
      print("{name} can't attack; they're knocked out!".format(name=self.name))
    elif player.health <= 0 :
      print("{name1} can't attack; {name2} is knocked out!".format(name1=self.name, name2=player.name))
    else :
      player.health -= self.damage*3/2
      if player.health <= 0 :
        print("{name1} kicks {name2}.".format(name1=self.name, name2=player.name))
        print("{name2} has been knocked out!".format(name2=player.name))
        print("You lose!")
      else:
        print("{name1} kicks {name2}. {name2} takes {damage} damage!".format(name1=self.name, name2=player.name, damage=int(round(self.damage,0))))
        
  # Use a special attack on the player 
  def use_special(self, player):
    if self.special_act == "Potion":
      if self.health <= 0 :
        print("{name} can't use a potion; they're knocked out!".format(name=self.name))
      else :
        self.health += 5
        print("{name} used a potion and regained 5 health!".format(name=self.name))       

    elif self.special_act == "Flying Kick":
      if self.health <= 0 :
        print("{name} can't attack; they're knocked out!".format(name=self.name))
      elif player.health <= 0 :
        print("{name1} can't attack; {name2} is knocked out!".format(name1=self.name, name2=player.name))
      else :
        player.health -= self.damage*2
        if player.health <= 0:
          print("{name1} used a flying kick on {name2}.".format(name1=self.name, name2=player.name))       
          print("{name2} has been knocked out!".format(name2=player.name))
          print("You lose!")
        else:
          print("{name1} used a flying kick on {name2}. {name2} takes {damage} damage!".format(name1=self.name, name2=player.name, damage=int(self.damage*2)))       

    elif self.special_act == "Multiple Jabs":
      if self.health <= 0 :
        print("{name} can't attack; they're knocked out!".format(name=self.name))
      elif player.health <= 0 :
        print("{name1} can't attack; {name2} is knocked out!".format(name1=self.name, name2=player.name))
      else :
        player.health -= self.damage*3
        if player.health <= 0:
          print("{name1} used multiple jabs on {name2}.".format(name1=self.name, name2=player.name))       
          print("{name2} has been knocked out!".format(name2=player.name))
          print("You lose!")
        else:
          print("{name1} used multiple jabs on {name2}. {name2} takes {damage} damage!".format(name1=self.name, name2=player.name, damage=int(self.damage*3)))       

    elif self.special_act == "Drain":
      if self.health <= 0 :
        print("{name} can't attack; they're knocked out!".format(name=self.name))
      elif player.health <= 0 :
        print("{name1} can't attack; {name2} is knocked out!".format(name1=self.name, name2=player.name))
      else :     
        player.health -= self.damage
        self.health += self.damage
        if player.health <= 0:
          print("{name1} took {damage} health from {name2}.".format(name1=self.name, name2=player.name, damage=round(self.damage,0)))         
          print("{name2} has been knocked out!".format(name2=player.name))
          print("You lose!")
        else:
          print("{name1} used drain. {name1} took {damage} health from {name2}!".format(name1=self.name, name2=player.name, damage=int(self.damage)))         
        



# Create Player class
class Player:
  def __init__(self, name, level, damage, special_act, health=0):
    self.name = name
    self.level = level
    self.health = level * 5
    self.damage = damage   
    self.special_act = special_act

  # Describe the Player 
  def __repr__(self):
    description = "This level {level} player is called {name}. They have {health} points of health and deal {damage} damage. Their special action is {special_act}.".format(level = self.level, name = self.name, health = self.health, damage = self.damage, special_act = self.special_act)
    return description

  # Punch the enemy
  def punch(self, enemy):
    if self.health <= 0 :
      print("{name} can't attack; she's knocked out!".format(name=self.name))
    elif enemy.health <= 0 :
      print("{name1} can't attack; {name2} is knocked out!".format(name1=self.name, name2=enemy.name))
    else :
      enemy.health -= self.damage
      if enemy.health <= 0 :
        self.level += 1
        print("{name} has been knocked out!".format(name=enemy.name))
      else:
        print("{name} took {damage} damage!".format(name=enemy.name, damage=int(self.damage)))   

  # Kick the enemy
  def kick(self, enemy):
    if self.health <= 0 :
      print("{name} can't attack; she's knocked out!".format(name=self.name))
    elif enemy.health <= 0 :
      print("{name1} can't attack; {name2} is knocked out!".format(name1=self.name, name2=enemy.name))
    else :
      enemy.health -= self.damage*3/2 
      if enemy.health <= 0 :
        self.level +=1
        print("{name} has been knocked out!".format(name=enemy.name))
      else:
        print("{name} took {damage} damage!".format(name=enemy.name, damage=int(round(self.damage*3/2,0)))) 

  # Taunt the enemy
  def taunt(self, enemy):
    if self.health <= 0 :
      print("{name1} can't taunt {name2}; she's knocked out!".format(name1=self.name, name2=enemy.name))
    elif enemy.health <= 0 :
      print("{name1} calls {name2} a doodoo-head, which is pretty fucked up because they're passed out...".format(name1=self.name, name2=enemy.name))
    else:
      print("{name1} calls {name2} a dirty landlubber. They don't know what to say to that...".format(name1=self.name, name2=enemy.name))

  # Use a special attack
  def use_special(self, enemy):
    if self.special_act == "Potion":
      if self.health <= 0 :
        print("{name} can't use a potion; she's knocked out!".format(name=self.name))
      else :
        self.health += 5
        print("{name} regained 5 health!".format(name=self.name))      

    elif self.special_act == "Flying Kick":
      if self.health <= 0 :
        print("{name} can't attack; they're knocked out!".format(name=self.name))
      elif enemy.health <= 0 :
        print("{name1} can't attack; {name2} is knocked out!".format(name1=self.name, name2=enemy.name))
      else :
        enemy.health -= self.damage*2
        if enemy.health <= 0:    
          self.level += 1
          print("{name2} has been knocked out!".format(name2=enemy.name))
        else:
          print("{name1} used a flying kick on {name2}. {name2} takes {damage} damage!".format(name1=self.name, name2=enemy.name, damage=int(self.damage*2)))       

    elif self.special_act == "Multiple Jabs":
      if self.health <= 0 :
        print("{name} can't attack; she's knocked out!".format(name=self.name))
      elif enemy.health <= 0 :
        print("{name1} can't attack; {name2} is knocked out!".format(name1=self.name, name2=enemy.name))
      else :
        enemy.health -= self.damage*3
        if enemy.health <= 0 :   
          self.level += 1
          print("{name2} has been knocked out!".format(name2=enemy.name))
        else:
          print("{name1} used multiple jabs on {name2}. {name2} takes {damage} damage!".format(name1=self.name, name2=enemy.name, damage=int(self.damage*3)))       

    elif self.special_act == "Drain":
      if self.health <= 0 :
        print("{name} can't attack; she's knocked out!".format(name=self.name))
      elif enemy.health <= 0 :
        print("{name1} can't attack; {name2} is knocked out!".format(name1=self.name, name2=enemy.name))
      else :     
        enemy.health -= self.damage
        self.health += self.damage
        if enemy.health <= 0:     
          self.level += 1
          print("{name2} has been knocked out!".format(name2=enemy.name))
        else:
          print("{name1} used drain. {name1} took {damage} health from {name2}!".format(name1=self.name, name2=enemy.name, damage=int(self.damage)))         
 


def gameplay():
    # Create 2 main player characters
    Misako = Player(name="Misako", level=5, damage=10, special_act="Drain")
    Kyoko = Player(name="Kyoko", level=5, damage=10, special_act="Flying Kick")

    # Create enemies
    Bully = Enemy(name=random.choice(["Bully Dino", "Bully Tina", "Bully Jerome"]), 
                        level = 2, damage = 3, special_act = "Drain")
    
    School_Girl = Enemy(name=random.choice(["School Girl Susan", "School Girl Kelly", "School Girl Hannah"]),
                        level = 3, damage = 4, special_act = "Multiple Jabs")
    
    Punk = Enemy(name=random.choice(["Punk Danielle", "Punk Zoe", "Punk Harris"]), 
                        level = 4, damage = 8, special_act = "Flying Kick")
    
    Tiger_Man = Enemy(name=random.choice(["Tiger Man Bob", "Tiger Man Joe", "Tiger Man Zeus"]),
                        level = 5, damage = 10, special_act = "Potion")
    
    Yakuza = Enemy(name=random.choice(["Yakuza Tim", "Yakuza Michelle", "Yakuza Lee"]),  
                        level = 6, damage = 11, special_act = "Multiple Jabs")
    
    # Create enemy list
    Enemy_List = [Bully, School_Girl, Punk, Tiger_Man, Yakuza]    
    
    # Have the player choose their fighter
    Choice = input("Do you want to play as Misako or Kyoko? ")
    
    # Make sure the player chose a valid fighter
    while Choice not in ("Misako","Kyoko"):
      Choice = input("Please enter either Misako or Kyoko. ")
    print("")
    
    # Set the Active Player
    if Choice == "Misako":
        Active_Player = Misako
    else:
        Active_Player = Kyoko
    
    # Loop through all the enemies
    for enemy in Enemy_List:
        Active_Enemy = enemy
        
        # Only initiate conflict if the player is conscious
        if Active_Player.health > 0 :
            # Initiate conflict
            print("You are attacked by " + 
                  Active_Enemy.name +
                  "!")
            print("")
        
        # Continue conflict while everyone is conscious
        while Active_Player.health > 0 and Active_Enemy.health > 0 :
        
            # Ask the player for their move 
            print("Which attack would you like to use?")
            print("Taunt, Punch, Kick, or Special Attack")
            Attack = input("Enter your attack: ")
             
            # Make sure the player chose a valid move 
            while Attack not in ("Taunt", "Punch", "Kick", "Special Attack"):
              Attack = input("Please pick a valid attack: ")   
            
            # Attack 
            if Attack == "Taunt":
                Active_Player.taunt(Active_Enemy)
                print("")
            elif Attack == "Punch":
                Active_Player.punch(Active_Enemy)
                print("")
            elif Attack == "Kick":
                Active_Player.kick(Active_Enemy)
                print("")
            elif Attack == "Special Attack":
                Active_Player.use_special(Active_Enemy)
                print("")
                
            # Break if someone's no longer conscious
            if Active_Player.health <= 0 or Active_Enemy.health <= 0 :
                break
            
            # Get attacked
            Enemy_Attack = random.choice(["Slap", "Punch", "Kick", "Special Attack"])
             
            if Enemy_Attack == "Slap":
                Active_Enemy.slap(Active_Player)
                print("")
            elif Enemy_Attack == "Punch":
                Active_Enemy.punch(Active_Player)
                print("")
            elif Enemy_Attack == "Kick":
                Active_Enemy.kick(Active_Player)
                print("")
            elif Enemy_Attack == "Special Attack":
                Active_Enemy.use_special(Active_Player)
                print("")   
    
    # If the player is still conscious after knocking out all enemies, they've won!
    if Active_Player.health > 0:
        print("You won!")
        print("")
        
    # Whether they've won or lost, they can play again:
    print("Would you like to play again?")
    print("Yes or No")
    Again = input("")
    
    # Make sure the player chose a valid option
    while Again not in ("Yes","No"):
      Again = input("Please enter either Yes or No. ") 
    
    # If they chose play again, allow them to play again
    if Again == "Yes":
      gameplay()
        
    
gameplay()


#To Do 
### Add more comments
### Remove extraneous elements ("X can't attack b/c X/Y is knocked out")
### Make sure drain can only remove as much health as a character actually has
### Add more taunts 
### Convert all damage to a multiple of level?
### Additional text cleaning?

### (DONE) Create a loop to fight all villains 
### (DONE) Create You Win text
### (DONE) Create Play Again?/Try Again? process after winning/losing 
### (DONE) Add a cool header
