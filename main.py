class battlefield:
    size = int()
    field = []
    def __init__(self, size):
        self.size = size


    # destroyed = [(),(),()]
    def drawField (self,destroyed):
       for i in range(0,self.size):
           for j in range(0,self.size):
               self.field.append("|0|")

       for i in range(0,len(destroyed)):
           for j in range (0,len(destroyed)):
               self.field.pop([i][j])
               self.field.insert([i][j],"|*|")





a = battlefield(6)
b = [(0,0)]
a.drawField(b)

print(a.field)
# a = [(1,0),(3,5),(7,10)]
#
# print(len(a))
#
# b = [[1,2,3,11,12],[4,5,6,7,8]]
# print(b[1][0])