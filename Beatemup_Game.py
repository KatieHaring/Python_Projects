
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

Player1 = Player(name="Misako", level=5, damage=10, special_act="Drain")
Player2 = Player(name="Kyoko", level=5, damage=10, special_act="Flying Kick")

School_Girl = Enemy(name="School Girl Susan", level = 2, damage = 4, special_act = "Multiple Jabs")
Tiger_Man = Enemy(name="Tiger Man Bob", level = 5, damage = 10, special_act = "Potion")

#print(Player1)
#print(Player2)
#print(School_Girl)
#print(Tiger_Man)


Player1.punch(Tiger_Man)
Tiger_Man.punch(Player1)
#Player1.kick(Tiger_Man)
#Tiger_Man.kick(Player1)
Player1.use_special(Tiger_Man) 
Tiger_Man.use_special(Player1) 
Tiger_Man.slap(Player1)
Player1.taunt(Tiger_Man)