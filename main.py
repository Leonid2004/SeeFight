#Возможно я немного отошел от задания но я решил немного сделать по другому с
#точки зрения ООП. Решил описать через 3 класса,было так немного удобнее(Главное же что бы игра работала)
#вот как тут:
#
#


class player:
    theTurn = True
    attackArea = []

    def canIattack(self):
        return theTurn
    def attack(self,attackArea):
        pass
 
class AI:
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
            print(attackFieldPlaceConverter)

       for i in range(0,(self.size*self.size)):
               self.field.append("|0|")

       for i in range(0,len(attackFieldPlaceConverter)):
               self.field.pop(attackFieldPlaceConverter[i])
               self.field.insert(attackFieldPlaceConverter[i],"|*|")



a = battlefield(8)
b = [(1,5),(0,0),(0,2)]

a.fillField(b)

a.drawField()
# a = [(1,0),(3,5),(7,10)]
#
# print(len(a))
#
# b = [[1,2,3,11,12],[4,5,6,7,8]]
# print(b[1][0])
