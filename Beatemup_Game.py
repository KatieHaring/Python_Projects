import random



#Create Enemy class
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
      print("{name} can't slap the player; they're knocked out!".format(name=self.name))
    elif player.health <= 0 :
      print("{name} slaps the player...which is super fucked up, because they're passed out...".format(name=self.name))
    else :
      print("{name} slaps the player. It doesn't hurt them, but it's super rude.".format(name=self.name))

  def punch(self, player):
    if self.health <= 0 :
      print("{name} can't attack; they're knocked out!".format(name=self.name))
    elif player.health <= 0 :
      print("{name} can't attack; the player is knocked out!".format(name=self.name))
    else :
      player.health -= self.damage
      if player.health <= 0 :
        print("The player has been knocked out!")
      else:
        print("The player took {damage} damage!".format(damage=self.damage))

  def kick(self, player):
    if self.health <= 0 :
      print("{name} can't attack; they're knocked out!".format(name=self.name))
    elif player.health <= 0 :
      print("{name} can't attack; the player is knocked out!".format(name=self.name))
    else :
      player.health -= self.damage*3/2
      if player.health <= 0 :
        print("The player has been knocked out!")
      else:
        print("The player took {damage} damage!".format(damage=self.damage*3/2))
        
  def use_special(self, player):
    if self.special_act == "Potion":
      if self.health <= 0 :
        print("{name} can't use a potion; they're knocked out!".format(name=self.name))
      else :
        self.health += 5
        print("{name} regained 5 health!".format(name=self.name))       

    elif self.special_act == "Flying Kick":
      if self.health <= 0 :
        print("{name} can't attack; they're knocked out!".format(name=self.name))
      elif player.health <= 0 :
        print("{name} can't attack; the player is knocked out!".format(name=self.name))
      else :
        player.health -= self.damage*2
        print("The player took {damage} damage!".format(damage=self.damage*2))       

    elif self.special_act == "Multiple Jabs":
      if self.health <= 0 :
        print("{name} can't attack; they're knocked out!".format(name=self.name))
      elif player.health <= 0 :
        print("{name} can't attack; the player is knocked out!".format(name=self.name))
      else :
        player.health -= self.damage*3
        print("The player took {damage} damage!".format(damage=self.damage*3))  

    elif self.special_act == "Drain":
      if self.health <= 0 :
        print("{name} can't attack; they're knocked out!".format(name=self.name))
      elif player.health <= 0 :
        print("{name} can't attack; the player is knocked out!".format(name=self.name))
      else :     
        player.health -= self.damage
        self.health += self.damage
        print("{name} took {damage} health from the player!".format(name=self.name, damage=self.damage))  



#Create Player class
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
      print("{name} can't attack; they're knocked out!".format(name=self.name))
    elif enemy.health <= 0 :
      print("{name} can't attack; the enemy is knocked out!".format(name=self.name))
    else :
      enemy.health -= self.damage
      if enemy.health <= 0 :
        print("{name} has been knocked out!".format(name=enemy.name))
      else:
        print("{name} took {damage} damage!".format(name=enemy.name, damage=self.damage))   

  def kick(self, enemy):
    if self.health <= 0 :
      print("{name} can't attack; they're knocked out!".format(name=self.name))
    elif enemy.health <= 0 :
      print("{name} can't attack; the enemy is knocked out!".format(name=self.name))
    else :
      enemy.health -= self.damage*3/2 
      if enemy.health <= 0 :
        print("{name} has been knocked out!".format(name=enemy.name))
      else:
        print("{name} took {damage} damage!".format(name=enemy.name, damage=self.damage*3/2)) 

  def taunt(self, enemy):
    if self.health <= 0 :
      print("{name} can't taunt the enemy; they're knocked out!".format(name=self.name))
    elif enemy.health <= 0 :
      print("{name} calls the enemy a doodoo-head, which is pretty fucked up because they're passed out...".format(name=self.name))
    else:
      print("{name} calls the enemy a dirty landlubber. They don't know what to say to that...".format(name=self.name))

  def use_special(self, enemy):
    if self.special_act == "Potion":
      if self.health <= 0 :
        print("{name} can't use a potion; they're knocked out!".format(name=self.name))
      else :
        self.health += 5
        print("{name} regained 5 health!".format(name=self.name))      

    elif self.special_act == "Flying Kick":
      if self.health <= 0 :
        print("{name} can't attack; they're knocked out!".format(name=self.name))
      elif enemy.health <= 0 :
        print("{name} can't attack; the enemy is knocked out!".format(name=self.name))
      else :
        enemy.health -= self.damage*2
        print("{name} took {damage} damage!".format(name=enemy.name, damage=self.damage*2))     

    elif self.special_act == "Multiple Jabs":
      if self.health <= 0 :
        print("{name} can't attack; they're knocked out!".format(name=self.name))
      elif enemy.health <= 0 :
        print("{name} can't attack; the enemy is knocked out!".format(name=self.name))
      else :
        enemy.health -= self.damage*3
        print("{name} took {damage} damage!".format(name=enemy.name, damage=self.damage*3))  

    elif self.special_act == "Drain":
      if self.health <= 0 :
        print("{name} can't attack; they're knocked out!".format(name=self.name))
      elif enemy.health <= 0 :
        print("{name} can't attack; the enemy is knocked out!".format(name=self.name))
      else :     
        enemy.health -= self.damage
        self.health += self.damage
        print("{name} took {damage} health from {enemy}!".format(name=self.name, damage=self.damage, enemy=enemy.name))  



#Create 2 main player types
Misako = Player(name="Misako", level=5, damage=10, special_act="Drain")
Kyoko = Player(name="Kyoko", level=5, damage=10, special_act="Flying Kick")



#Create enemies
Skeezeball = Enemy(name=random.choice(["Skeezeball Wade", "Skeezeball Zach", "Skeezeball Stan"]),
                    level = 1, damage = 1, special_act="Drain")

Bully = Enemy(name=random.choice(["Bully Dino", "Bully Tina", "Bully Zachariah"]), 
                    level = 2, damage = 3, special_act = "Drain")

School_Girl = Enemy(name=random.choice(["School Girl Susan", "School Girl Kelly", "School Girl Hannah"]),
                    level = 3, damage = 4, special_act = "Multiple Jabs")

Punk = Enemy(name=random.choice(["Punk Danielle", "Punk Zoe", "Punk Harris"]), 
                    level = 4, damage = 8, special_act = "Flying Kick")

Tiger_Man = Enemy(name=random.choice(["Tiger Man Bob", "Tiger Man Joe", "Tiger Man Zeus"]),
                    level = 5, damage = 10, special_act = "Potion")

Yakuza = Enemy(name=random.choice(["Yakuza Tim", "Yakuza Michelle", "Yakuza Lee"]),  
                    level = 6, damage = 11, special_act = "Multiple Jabs")





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
    Active_Enemy = random.choice([Skeezeball, Bully, School_Girl, Punk, Tiger_Man, Yakuza])  
      
    # Initiate conflict
    print("You are attacked by " + 
          Active_Enemy.name +
          "!")
    print("")
    
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
    elif Attack == "Punch":
        Active_Player.punch(Active_Enemy)
    elif Attack == "Kick":
        Active_Player.kick(Active_Enemy)
    elif Attack == "Special Attack":
        Active_Player.use_special(Active_Enemy)
        
    # Get attacked
    

gameplay()
