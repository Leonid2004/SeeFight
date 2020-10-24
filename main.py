#Возможно я немного отошел от задания но я решил немного сделать по другому с
#точки зрения ООП. Решил описать через 3 класса,было так немного удобнее(Главное же что бы игра работала)
#вот как тут:
#
#

import random

class player:
    theTurn = bool()
    attackArea = []
    
    def __init__(self, _theTurn):
        self.theTurn = _theTurn
        
    def canIattack(self):
        return self.theTurn
    
    def attack(self,attackPlace):
        self.attackArea.append(attackPlace)
        self.theTurn = False

        return self.attackArea




             
 
class AI(player):
  theTurn = bool()
  attackArea = []
  FieldSize = int()
  def __init__(self,theTurn):
      super().__init__(theTurn)
      
  def attack(self,attackPlace):
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


user = player(True)
theField = battlefield(6)
theField.fillField(user.attackArea)
theField.drawField()
print("")
if user.canIattack() == True:
    theField.fillField(user.attack((0,1)))
    theField.drawField()


machine = AI(True)
print(machine.canIattack())