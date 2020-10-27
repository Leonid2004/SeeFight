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
         counter = 0
         while counter < 7:
              print(counter)
              if counter == 0:
                FirstCellStr = int(input("Line of starting point for the big ship:"))
                FirstCellCol = int(input("Column of starting point for the big ship:"))
                Dir = str(input("Direction for the ship (u - up d - down r - right l - left):"))
              elif counter > 0 and counter < 3:
                FirstCellStr = int(input("Line of starting point for the medium ship:"))
                FirstCellCol = int(input("Column of starting point for the medium ship:"))
                Dir = str(input("Direction for the ship (u - up d - down r - right l - left):"))
              elif counter >=3:
                FirstCellStr = int(input("Line of starting point for the small ship:"))
                FirstCellCol = int(input("Column of starting point for the small ship:"))

                


              Direction.append(Dir)
              strs = FirstCellStr
              colmns = FirstCellCol
              cntr = 0
              for j in range(0, fieldSize):
                  cntr += strs
              cntr += colmns
              flag = False
              self.Ships[counter].append(cntr)
              for o in range(0, len(self.Ships)):
                     if flag == True:
                        break
                     for j in range(0, len(self.Ships[o])):
                         if  flag == True:
                             break
                         for k in range(o + 1, len(self.Ships)):
                             if flag == True:
                                 break
                             for l in range(0, len(self.Ships[k])):
                                 if self.Ships[o][j] == self.Ships[k][l]:
                                     print("You already shot in this place, enter another one", k, l, o, j)
                                     counter -= 1
                                     flag = True
                                     self.Ships[k].pop(l)
                                     break


              counter += 1
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
                   ### ##

         # WrongAnswers = []
         # for i in range(0,len(self.Ships)):
         #     for j in range(0,len(self.Ships[i])):
         #         for k in range(i+1,len(self.Ships)):
         #           for l in range(0,len(self.Ships[k])):
         #              if self.Ships[i][j] == self.Ships[k][l]:
         #                  print("Too near!",k,l,i,j)
         #                  WrongAnswers.append((i,j,k,l))



         return self.Ships

    def printShips(self,ships):
        print(ships)



             
 
class AI(player):
  attackArea = []
  Ships = [[], [], [], [], [], [], []]
  dirr = "ldru"
  Direction = []
  def attack(self,FieldSize):
      place1 = random.randint(0,FieldSize)
      place2 = random.randint(0,FieldSize)
      self.attackArea.append((place1,place2))
      return self.attackArea

  def putShips(self,FieldSize):
      for i in range(0, 3):
          self.Direction.append(random.choice(self.dirr))
      counter = 0
      for i in range(0,7):
          if i == 0:
            placeStr = random.randint(3, FieldSize-4)
            placeCol = random.randint(3, FieldSize-4)
          if i > 0 and i < 3:
             placeStr = random.randint(2, FieldSize-3)
             placeCol = random.randint(2, FieldSize-3)
          else:
             placeStr = random.randint(0, FieldSize-1)
             placeCol = random.randint(0, FieldSize-1)
                      
          cntr = 0
          for j in range(0, FieldSize):
            cntr += placeStr
            print(cntr)
            print("")
          cntr += placeCol
          print(cntr)
          self.Ships[i].append(cntr)
      print(self.Ships)
      print(self.Direction)
      for i in range(0, 3):#############problem I guess it it because we shoud substract 1 form the size idk
            if i == 0:  # big ship
                if self.Direction[i] == 'l':#error is here if the big ship or medium can go out of boundaries
                    self.Ships[i].append(self.Ships[i][0] - 1)
                    self.Ships[i].append(self.Ships[i][0] - 2)
                if self.Direction[i] == 'r':
                    self.Ships[i].append(self.Ships[i][0] + 1)
                    self.Ships[i].append(self.Ships[i][0] + 2)
                if self.Direction[i] == 'u':
                    self.Ships[i].append(self.Ships[i][0] - FieldSize)
                    self.Ships[i].append(self.Ships[i][0] - (2 * FieldSize))
                if self.Direction[i] == 'd':
                    self.Ships[i].append(self.Ships[i][0] + FieldSize)
                    self.Ships[i].append(self.Ships[i][0] + (2 * FieldSize))

            if i > 0 and i < 3:
                if self.Direction[i] == 'l':
                    self.Ships[i].append(self.Ships[i][0] - 1)
                if self.Direction[i] == 'r':
                    self.Ships[i].append(self.Ships[i][0] + 1)
                if self.Direction[i] == 'u':
                    self.Ships[i].append(self.Ships[i][0] - FieldSize)
                if self.Direction[i] == 'd':
                    self.Ships[i].append(self.Ships[i][0] + FieldSize)
      return self.Ships




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
     print(" ");

    def fillField (self,attacked,ships):
       attackFieldPlaceConverter = []

       for i in range(0,len(attacked)):
         #  for j in range(0,self.size):
            strs = attacked[i][0]
            colmns = attacked[i][1]
            cntr = 0
            for j in range(0,self.size):
             cntr += strs
            cntr += colmns
            attackFieldPlaceConverter.append(cntr)

       for i in range(0,(self.size*self.size)):
               self.field.append("|0|")

       for i in range(0,7):
           for j in range(0,len(ships[i])):
            self.field.pop(ships[i][j])
            self.field.insert(ships[i][j],"|1|")

       for i in range(0,len(attackFieldPlaceConverter)):
               hitTheShip = False
               self.field.pop(attackFieldPlaceConverter[i])
               for k in range(0,7):
                   for j in range(0,len(ships[k])):
                       if attackFieldPlaceConverter[i] == ships[k][j]:
                           hitTheShip = True

               if hitTheShip == True:
                    self.field.insert(attackFieldPlaceConverter[i],"|X|")
               else:
                   self.field.insert(attackFieldPlaceConverter[i], "|T|")

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
#         y = int(input("\nAttacking column= "))
#         person.attack((x,y))
#         UserTurn = False
#         BotTurn = True
#
#     elif BotTurn == True:
#         bot.attack(theSizeOfField)
#         BotTurn = False
#         UserTurn = True

########################################
# b = battlefield(8)
# a = player()
# a.putShips(8)
# x = int(input("attack Line"))
# y = int(input("attack Column"))
# a.attack((x,y))
#
# machine = AI()
#
# AIBattleField = battlefield(8)
# AIBattleField.fillField((),a.Ships)
# AIBattleField.drawField()
# AIBattleField.fillField(a.attackArea,a.Ships)
# AIBattleField.drawField()
machine = AI()
machine1 = battlefield(8)
machine1.fillField(machine.attackArea,machine.putShips(8))
machine1.drawField()
