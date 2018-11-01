class Score_processing:
    def loadScore( self ):
        f = open('scores.txt')
        self.data = {}
        while True:
            line = f.readline()
            if line=='':
                break
            row = line.strip().split(',')
            if row[0] not in self.data:
                self.data[row[0]] = {}
            self.data[row[0]][row[1]] = row[2::]
            self.data[row[0]][row[1]] = [int(x) for x in self.data[row[0]][row[1]]]
        
    def getSubject( self ):
        subj = set()
        for sub in self.data.values():
            subj.update(set(sub.keys()))
        return list(subj)
    
    def getScore( self, subject ):
        scores = [(name, sum(score[subject])) for name, score in self.data.items()]
        scores.sort(key = lambda x:x[1], reverse = True)
        return scores

    def getScoreStat( self, scores ):
        scores.sort(key = lambda x:x[1], reverse = False)
        smin = scores[0]
        smax = scores[-1]
        raw = zip(*scores)
        average = sum(raw[1])/len(scores)
        return smin, smax, average

def main():
    obj = Score_processing()
    obj.loadScore()
    for sub in obj.getSubject():
        scores = obj.getScore(sub)
        print(scores)
        print(obj.getScoreStat(scores))
if __name__ == "__main__":
    main()
