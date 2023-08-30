
import random



# Create Enemy class
class Enemy:
  def __init__(self, name, level, damage, special_act, health=0):
    self.name = name
    self.level = level
    self.health = level * 5
    self.damage = damage
    self.special_act = special_act

  def __repr__(self):
    description = "This level {level} enemy is called {name}. They have {health} points of health and deal {damage} damage. Their special action is {special_act}.".format(level = self.level, name = self.name, health = self.health, damage = self.damage, special_act = self.special_act)
    return description

  def slap(self, player):
    if self.health <= 0 :
      print("{name1} can't slap {name2}; they're knocked out!".format(name1=self.name, name2=player.name))
    elif player.health <= 0 :
      print("{name1} slaps {name2}...which is super fucked up, because she's passed out...".format(name1=self.name, name2=player.name))
    else :
      print("{name1} slaps {name2}. It doesn't hurt her, but it's super rude.".format(name1=self.name, name2=player.name))

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
        print("{name1} punches {name2}. {name2} takes {damage} damage!".format(name1=self.name, name2=player.name, damage=self.damage))

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
        print("{name1} kicks {name2}. {name2} takes {damage} damage!".format(name1=self.name, name2=player.name, damage=self.damage))
        
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
          print("{name1} used a flying kick on {name2}. {name2} takes {damage} damage!".format(name1=self.name, name2=player.name, damage=self.damage*2))       

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
          print("{name1} used multiple jabs on {name2}. {name2} takes {damage} damage!".format(name1=self.name, name2=player.name, damage=self.damage*3))       

    elif self.special_act == "Drain":
      if self.health <= 0 :
        print("{name} can't attack; they're knocked out!".format(name=self.name))
      elif player.health <= 0 :
        print("{name1} can't attack; {name2} is knocked out!".format(name1=self.name, name2=player.name))
      else :     
        player.health -= self.damage
        self.health += self.damage
        if player.health <= 0:
          print("{name1} took {damage} health from {name2}.".format(name1=self.name, name2=player.name, damage=self.damage))         
          print("{name2} has been knocked out!".format(name2=player.name))
          print("You lose!")
        else:
          print("{name1} took {damage} health from {name2}.".format(name1=self.name, name2=player.name, damage=self.damage))         
        



# Create Player class
class Player:
  def __init__(self, name, level, damage, special_act, health=0):
    self.name = name
    self.level = level
    self.health = level * 5
    self.damage = damage   
    self.special_act = special_act

  def __repr__(self):
    description = "This level {level} player is called {name}. They have {health} points of health and deal {damage} damage. Their special action is {special_act}.".format(level = self.level, name = self.name, health = self.health, damage = self.damage, special_act = self.special_act)
    return description

  def punch(self, enemy):
    if self.health <= 0 :
      print("{name} can't attack; she's knocked out!".format(name=self.name))
    elif enemy.health <= 0 :
      print("{name1} can't attack; {name2} is knocked out!".format(name1=self.name, name2=enemy.name))
    else :
      enemy.health -= self.damage
      if enemy.health <= 0 :
        print("{name} has been knocked out!".format(name=enemy.name))
      else:
        print("{name} took {damage} damage!".format(name=enemy.name, damage=self.damage))   

  def kick(self, enemy):
    if self.health <= 0 :
      print("{name} can't attack; she's knocked out!".format(name=self.name))
    elif enemy.health <= 0 :
      print("{name1} can't attack; {name2} is knocked out!".format(name1=self.name, name2=enemy.name))
    else :
      enemy.health -= self.damage*3/2 
      if enemy.health <= 0 :
        print("{name} has been knocked out!".format(name=enemy.name))
      else:
        print("{name} took {damage} damage!".format(name=enemy.name, damage=self.damage*3/2)) 

  def taunt(self, enemy):
    if self.health <= 0 :
      print("{name1} can't taunt {name2}; she's knocked out!".format(name1=self.name, name2=enemy.name))
    elif enemy.health <= 0 :
      print("{name1} calls {name2} a doodoo-head, which is pretty fucked up because they're passed out...".format(name1=self.name, name2=enemy.name))
    else:
      print("{name1} calls {name2} a dirty landlubber. They don't know what to say to that...".format(name1=self.name, name2=enemy.name))

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
          print("{name2} has been knocked out!".format(name2=enemy.name))
        else:
          print("{name1} used a flying kick on {name2}. {name2} takes {damage} damage!".format(name1=self.name, name2=enemy.name, damage=self.damage*2))       

    elif self.special_act == "Multiple Jabs":
      if self.health <= 0 :
        print("{name} can't attack; she's knocked out!".format(name=self.name))
      elif enemy.health <= 0 :
        print("{name1} can't attack; {name2} is knocked out!".format(name1=self.name, name2=enemy.name))
      else :
        enemy.health -= self.damage*3
        if enemy.health <= 0 :   
          print("{name2} has been knocked out!".format(name2=enemy.name))
        else:
          print("{name1} used multiple jabs on {name2}. {name2} takes {damage} damage!".format(name1=self.name, name2=enemy.name, damage=self.damage*3))       

    elif self.special_act == "Drain":
      if self.health <= 0 :
        print("{name} can't attack; she's knocked out!".format(name=self.name))
      elif enemy.health <= 0 :
        print("{name1} can't attack; {name2} is knocked out!".format(name1=self.name, name2=enemy.name))
      else :     
        enemy.health -= self.damage
        self.health += self.damage
        if enemy.health <= 0:     
          print("{name2} has been knocked out!".format(name2=enemy.name))
        else:
          print("{name1} took {damage} health from {name2}.".format(name1=self.name, name2=enemy.name, damage=self.damage))         
 


# Create 2 main player types
Misako = Player(name="Misako", level=5, damage=10, special_act="Drain")
Kyoko = Player(name="Kyoko", level=5, damage=10, special_act="Flying Kick")



# Create enemies
Skeezeball = Enemy(name=random.choice(["Skeezeball Wade", "Skeezeball Zach", "Skeezeball Stan"]),
                    level = 1, damage = 1, special_act="Drain")

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

Enemy_List = [Skeezeball, Bully, School_Girl, Punk, Tiger_Man, Yakuza]



def gameplay():
    # Choose your fighter
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

    # Set the active enemy
    Active_Enemy = random.choice(Enemy_List)  
      
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
    
    
gameplay()


#To Do 
### Create a loop to fight all villains 
### Create You Win text
### Create Play Again?/Try Again? process after winning/losing 
### Change the enemy order to only have enemies at or below your level attack you
### Add level ups every time an enemy is defeated 
### Fix how some attack damages have decimals and some are integers
### Additional text cleaning?
