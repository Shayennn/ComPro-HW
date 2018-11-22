#std35: Phitchawat Lukkanathiti 6110503371
#date: 22NOV2018
#program: 01_census.py
#description: Calculating Population of abnormal area.

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

    def getData(self):
        return self.data
    
    def getArea(self):
        return self.area
    
    def getPop(self):
        return self.pop

if __name__ == "__main__":
    c = Census()
    print('Population')
    for area,pop in c.getPop().items():
        print('\t Area:',area,':',format(pop,'.4f'))
