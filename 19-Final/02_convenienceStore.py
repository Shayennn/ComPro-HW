#std35: Phitchawat Lukkanathiti 6110503371
#date: 22NOV2018
#program: 02_convenienceStore.py
#description: Filter by size

class Census:

    def __init__(self):
        self.pop = {1:[],2:[],3:[],4:[],5:[],6:[]}
        self._loadFile()
        self.area = [[
            self._calcPopReturnArea(x,y) for x in range(50)
        ] for y in range(50)]
        self._finalisePop()

    def _finalisePop(self):
        for area, pop in self.pop.items():
            self.pop[area] = sum(pop)/len(pop)

    def _calcPopReturnArea(self,x,y):
        area = self.whatArea(x,y)
        self.pop[area].append(self.data[y][x])
        return area

    def whatArea(self,x,y):
        if x < 15 and y < 16:
            return 1
        if x < 10:
            return 2
        if x < 15 or y >= 45:
            return 3
        if y <= x-15:
            return 6
        if y < 30:
            return 4
        return 5

    def _loadFile(self):
        self.data = []
        f = open('census2.txt')
        while True:
            line = f.readline()
            if not line:
                break
            self.data.append([int(x) for x in line.split()])
        f.close()

    def findArea(self,k):
        # When found it'll return top left and buttom right and pop
        area = []
        for y in range(50-k):
            for x in range(50-k):
                thisblock = []
                for row in self.area[y:y+k]:
                    thisblock.append(row[x:x+k])
                sumblockarea = self._sumBlock(thisblock)
                if sumblockarea/(k*k)==thisblock[0][0] and sumblockarea%(k*k) == 0:
                    thisblockPeople = []
                    for row in self.data[y:y+k]:
                        thisblockPeople.append(row[x:x+k])
                    area.append((thisblock[0][0],self._sumBlock(thisblockPeople),x,y,x+k,y+k))
        return area

    def _sumBlock(self,block):
        summ = 0
        for row in block:
            summ += sum(row)
        return summ


    def getData(self):
        return self.data
    
    def getArea(self):
        return self.area
    
    def getPop(self):
        return self.pop

if __name__ == "__main__":
    k = int(input('K: '))
    c = Census()
    afk = c.findArea(k)
    afk.sort(key=lambda x:x[1], reverse=True)
    print("Area",afk[0][0],'is the best with',format(afk[0][1]/(k*k),'.4f'),'people per km^2.')
    print("X:\t",afk[0][2]+1)
    print("Y:\t",afk[0][3]+1)
    print("X+K:\t",afk[0][4]+1)
    print("Y+K:\t",afk[0][5]+1)
