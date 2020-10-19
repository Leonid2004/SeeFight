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
       for i in range(0,(self.size*self.size)):
               self.field.append("|0|")

       for i in range(0,len(destroyed)):
               self.field.pop(destroyed[i])
               self.field.insert(destroyed[i],"|*|")




a = battlefield(6)
b = [0,2]

a.fillField(b)

a.drawField()
# a = [(1,0),(3,5),(7,10)]
#
# print(len(a))
#
# b = [[1,2,3,11,12],[4,5,6,7,8]]
# print(b[1][0])