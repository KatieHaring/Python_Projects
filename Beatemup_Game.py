
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
  def __init__(self, name, damage, special_act, health=0):
    self.name = name
    self.damage = damage
    self.health = damage * 5
    self.special_act = special_act

  # Describe the enemy
  def __repr__(self):
    description = "This enemy is called {name}. They have {health} points of health and deal {damage} damage. Their special action is {special_act}.".format(name = self.name, health = self.health, damage = self.damage, special_act = self.special_act)
    return description

  # Slap the player
  def slap(self, player):
    print("{name1} slaps {name2}.".format(name1=self.name, name2=player.name))
    print("It doesn't hurt her, but it's super rude.")

  # Punch the player
  def punch(self, player): 
    # Punching inflicts base damage
    player.health -= self.damage
    print("{name1} punches {name2}.".format(name1=self.name, name2=player.name))    
    if player.health <= 0 :
      print("{name2} has been knocked out!".format(name2=player.name))
      print("You lose!")
    else:    
      print("{name2} takes {damage} damage!".format(name2=player.name, damage=int(self.damage)))

  # Kick the player
  def kick(self, player):
    # Kicking inflicts base damage * 3/2
    player.health -= self.damage*3/2
    print("{name1} kicks {name2}.".format(name1=self.name, name2=player.name))    
    if player.health <= 0 :
      print("{name2} has been knocked out!".format(name2=player.name))
      print("You lose!")
    else:
      print("{name2} takes {damage} damage!".format(name2=player.name, damage=int(round(self.damage,0))))
        
  # Use a special attack on the player 
  def use_special(self, player):
    if self.special_act == "Sandwich":
      # Sandwiches restore 5 health 
      self.health += 5
      print("{name} eats a sandwich and regains 5 health!".format(name=self.name))       

    elif self.special_act == "Flying Kick":
      # Flying kicks do 2 times base damage
      player.health -= self.damage*2
      print("{name1} uses a flying kick on {name2}.".format(name1=self.name, name2=player.name)) 
      if player.health <= 0:
        print("{name2} has been knocked out!".format(name2=player.name))
        print("You lose!")
      else:            
        print("{name2} takes {damage} damage!".format(name2=player.name, damage=int(self.damage*2)))       

    elif self.special_act == "Multiple Jabs":
      # Multiple jabs do 3 times base damage 
      player.health -= self.damage*3
      print("{name1} uses multiple jabs on {name2}.".format(name1=self.name, name2=player.name))      
      if player.health <= 0:
        print("{name2} has been knocked out!".format(name2=player.name))
        print("You lose!")
      else:
        print("{name2} takes {damage} damage!".format(name2=player.name, damage=int(self.damage*3)))       

    elif self.special_act == "Drain":
      # Drain takes base damage health from the player
      begin_health = player.health
      player.health -= min(begin_health, self.damage)
      self.health += min(begin_health, self.damage)
      print("{name1} uses drain to take {damage} health from {name2}!".format(name1=self.name, name2=player.name, damage=int(round(min(begin_health, self.damage),0))))               
      if player.health <= 0:
        print("{name2} has been knocked out!".format(name2=player.name))
        print("You lose!")        



# Create Player class
class Player:
  def __init__(self, name, damage, special_act, health=0):
    self.name = name
    self.damage = damage       
    self.health = damage * 5
    self.special_act = special_act

  # Describe the Player 
  def __repr__(self):
    description = "This player is called {name}. They have {health} points of health and deal {damage} damage. Their special action is {special_act}.".format(name = self.name, health = self.health, damage = self.damage, special_act = self.special_act)
    return description

  # Punch the enemy
  def punch(self, enemy):
    # Punching inflicts base damage
    enemy.health -= self.damage
    print("{name1} punches {name2}.".format(name1=self.name, name2=enemy.name))    
    if enemy.health <= 0 :
      self.damage += 1
      print("{name} has been knocked out!".format(name=enemy.name))
    else:
      print("{name2} takes {damage} damage!".format(name2=enemy.name, damage=int(self.damage)))

  # Kick the enemy
  def kick(self, enemy):
    # Kicking inflicts base damage * 3/2
    enemy.health -= self.damage*3/2 
    print("{name1} kicks {name2}.".format(name1=self.name, name2=enemy.name))     
    if enemy.health <= 0 :
      self.damage +=1
      print("{name} has been knocked out!".format(name=enemy.name))
    else:
      print("{name2} takes {damage} damage!".format(name2=enemy.name, damage=int(round(self.damage*3/2,0)))) 
 
  # Taunt the enemy
  def taunt(self, enemy):
    # Create a list of possible taunts
    taunts = ["a dirty landlubber", "stinkier than Steubenville", "a pathetic snollygoster", "all hat and no cattle", 
              "less useful than belt dressing", "lacking in creativity", "a worthless gadabout"]
    # Pick a random taunt
    print("{name1} calls {name2} ".format(name1=self.name, name2=enemy.name) + random.choice(taunts) + ".")
    print("They don't know what to say to that...")    

  # Use a special attack on the enemy
  def use_special(self, enemy):
    if self.special_act == "Sandwich":
      # Sandwiches restore 5 health        
      self.health += 5
      print("{name} eats a sandwich and regains 5 health!".format(name=self.name))      

    elif self.special_act == "Flying Kick":
      # Flying kicks do 2 times base damage
      enemy.health -= self.damage*2
      print("{name1} uses a flying kick on {name2}.".format(name1=self.name, name2=enemy.name))            
      if enemy.health <= 0:    
        self.damage += 1
        print("{name2} has been knocked out!".format(name2=enemy.name))
      else:
        print("{name2} takes {damage} damage!".format(name2=enemy.name, damage=int(self.damage*2)))       

    elif self.special_act == "Multiple Jabs":
      # Multiple jabs do 3 times base damage 
      enemy.health -= self.damage*3
      print("{name1} uses a multiple jabs on {name2}.".format(name1=self.name, name2=enemy.name))     
      if enemy.health <= 0 :   
        self.damage += 1
        print("{name2} has been knocked out!".format(name2=enemy.name))
      else:     
        print("{name2} takes {damage} damage!".format(name2=enemy.name, damage=int(self.damage*3)))       

    elif self.special_act == "Drain":
      # Drain takes base damage health from the enemy
      begin_health = enemy.health 
      enemy.health -= min(self.damage, begin_health)
      self.health += min(self.damage, begin_health)
      print("{name1} uses drain to take {damage} health from {name2}!".format(name1=self.name, name2=enemy.name, damage=int(round(min(begin_health, self.damage),0))))         
      if enemy.health <= 0:     
        self.damage += 1
        print("{name2} has been knocked out!".format(name2=enemy.name))



def gameplay():
    # Create 2 main player characters
    Misako = Player(name="Misako", damage=7, special_act="Drain")
    Kyoko = Player(name="Kyoko", damage=8, special_act="Flying Kick")

    # Create enemies with random names and random specials
    Bully = Enemy(name=random.choice(["Bully Dino", "Bully Tina", "Bully Jerome"]), 
                        damage = 3, special_act = random.choice(["Sandwich","Flying Kick","Multiple Jabs","Drain"]))
    
    School_Girl = Enemy(name=random.choice(["School Girl Susan", "School Girl Kelly", "School Girl Hannah"]),
                        damage = 4, special_act = random.choice(["Sandwich","Flying Kick","Multiple Jabs","Drain"]))
    
    Punk = Enemy(name=random.choice(["Punk Danielle", "Punk Zoe", "Punk Harris"]), 
                        damage = 6, special_act = random.choice(["Sandwich","Flying Kick","Multiple Jabs","Drain"]))
    
    Tiger_Man = Enemy(name=random.choice(["Tiger Man Bob", "Tiger Man Joe", "Tiger Man Zeus"]),
                        damage = 8, special_act = random.choice(["Sandwich","Flying Kick","Multiple Jabs","Drain"]))
    
    Yakuza = Enemy(name=random.choice(["Yakuza Tim", "Yakuza Michelle", "Yakuza Lee"]),  
                        damage = 9, special_act = random.choice(["Sandwich","Flying Kick","Multiple Jabs","Drain"]))
    
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
            print("")
             
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
        print("You won!!!")
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
### (DONE) Replace level with damage
### (DONE) Add more taunts 
### (DONE) Change potion to sandwich
### (DONE) Give all enemies random attacks
### (DONE) Text cleaning
### (DONE) Add comments
