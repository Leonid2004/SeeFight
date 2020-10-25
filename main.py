#Возможно я немного отошел от задания но я решил немного сделать по другому с
#точки зрения ООП. Решил описать через 3 класса,было так немного удобнее(Главное же что бы игра работала)  ;)
#вот как тут:
#
#
#
# Поле :
# |0| - пусто
# |1| - корабль
# |X| - попадание по кораблю
# |T| - попадание в пустую клетку
#
#

import random

class player:
    attackArea = []
    Ships = [[],[],[],[],[],[],[]] #0 - Big, 1,2 - Medium, 3,4,5,6 - Small;

    def attack(self,attackPlace):
        self.attackArea.append(attackPlace)
        return self.attackArea

    def putShips(self,fieldSize):
         FirstCellCol = int()
         FirstCellStr = int()
         Dir = str()
         Direction = [] #up down right left

         for i in range(0,7):

              FirstCellStr = int(input("Line of starting point for the Ship:"))
              FirstCellCol = int(input("Column of starting point for the ship:"))
              Dir = str(input("Direction (u - up d - down r - right l - left):"))
              Direction.append(Dir)
              strs = FirstCellStr
              colmns = FirstCellCol
              cntr = 0
              for j in range(0, fieldSize):
                  cntr += strs
              cntr += colmns
              self.Ships[i].append(cntr)

         for i in range (0,3):
             if i == 0:#big ship
                if Direction[i] == "l":
                    self.Ships[i].append(self.Ships[i][0]-1)
                    self.Ships[i].append(self.Ships[i][0]-2)
                if Direction[i] == "r":
                    self.Ships[i].append(self.Ships[i][0]+1)
                    self.Ships[i].append(self.Ships[i][0]+2)
                if Direction[i] == "u":
                    self.Ships[i].append(self.Ships[i][0] - fieldSize)
                    self.Ships[i].append(self.Ships[i][0] - (2*fieldSize))
                if Direction[i] == "d":
                    self.Ships[i].append(self.Ships[i][0] + fieldSize)
                    self.Ships[i].append(self.Ships[i][0] + (2*fieldSize))

             if i > 0 and i < 3:
                if Direction[i] == "l":
                    self.Ships[i].append(self.Ships[i][0]-1)
                if Direction[i] == "r":
                    self.Ships[i].append(self.Ships[i][0]+1)
                if Direction[i] == "u":
                    self.Ships[i].append(self.Ships[i][0] - fieldSize)
                if Direction[i] == "d":
                    self.Ships[i].append(self.Ships[i][0] + fieldSize)

         return self.Ships

    def printShips(self,ships):
        print(ships)



             
 
class AI(player):
  attackArea = []
      
  def attack(self,FieldSize):
      place1 = random.randint(0,FieldSize)
      place2 = random.randint(0,FieldSize)
      self.attackArea.append((place1,place2))
      return self.attackArea

  def putShips(self):
      pass




class battlefield:
    size = int()
    field = []
    def __init__(self, size):
        self.size = size


    # destroyed = [(),(),()]
    def drawField(self):
     for i in range(0,(self.size*self.size)):
        if i % self.size == 0:
            print("\n")
        print(self.field[i],end="")

    def fillField (self,destroyed):
       attackFieldPlaceConverter = []

       for i in range(0,len(destroyed)):
         #  for j in range(0,self.size):
            strs = destroyed[i][0]
            colmns = destroyed[i][1]
            cntr = 0
            for j in range(0,self.size):
             cntr += strs
            cntr += colmns
            attackFieldPlaceConverter.append(cntr)

       for i in range(0,(self.size*self.size)):
               self.field.append("|0|")

       for i in range(0,len(attackFieldPlaceConverter)):
               self.field.pop(attackFieldPlaceConverter[i])
               self.field.insert(attackFieldPlaceConverter[i],"|*|")


#
# a = battlefield(8)
# b = [(1,5),(0,0),(0,2)]
# attackThisCell = [0,0]
# a.fillField(b)
#
# a.drawField()
#
# user = player()
# print(user.canIattack())
# user.attack(attackThisCell)
# print(user.canIattack())
# user.attack(attackThisCell)
# print(user.canIattack())
# # a = [(1,0),(3,5),(7,10)]
# #
# # print(len(a))
# #
# # b = [[1,2,3,11,12],[4,5,6,7,8]]
# # print(b[1][0])


# user = player(True)
# theField = battlefield(6)
# theField.fillField(user.attackArea)
# theField.drawField()
# print("")
# if user.canIattack() == True:
#     theField.fillField(user.attack((0,1)))
#     theField.drawField()
#
#
# machine = AI(True)
# print(machine.canIattack())


####################################################################################################################################
# UserTurn = bool(random.randint(0,1))
# BotTurn = bool(not UserTurn)
# print(UserTurn)
# print(BotTurn)
#
# person = player()
# bot = AI()
# theSizeOfField = int(input("\nEnter the size of battlefield = "))
#
# personField = battlefield(theSizeOfField)
# botField = battlefield(theSizeOfField)
# while True:
#     if UserTurn == True:
#         personField.fillField(bot.attackArea)
#         personField.drawField()
#         x = int(input("\nAttacking line = "))
#         y = int(input("\nAttacking column = "))
#         person.attack((x,y))
#         UserTurn = False
#         BotTurn = True
#
#     elif BotTurn == True:
#         bot.attack(theSizeOfField)
#         BotTurn = False
#         UserTurn = True



a = player()
a.putShips(5)
print(a.Ships)