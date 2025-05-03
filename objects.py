import random

class Deck:
    def __init__(self):
        self.suits = {'spades':0,'hearts':0,'diamonds':0,'clubs':0}
        count = [12,10,10,8]
        random.shuffle(count)
        suitlist =['spades','hearts','diamonds','clubs']
        for i in range(4):
            self.suits[suitlist[i]]=count[i]

        self.cards=[]
        for i in range(4):
            for j in range(self.suits[suitlist[i]]):
                self.cards.append(suitlist[i])
        random.shuffle(self.cards)


        #print(self.suits)  #display deck


    def goalSuit(self):
        map = {'spades':'clubs' , 'clubs':'spades','hearts':'diamonds','diamonds':'hearts'}
        suitlist =['spades','hearts','diamonds','clubs']
        for i in range(4):
            if self.suits[suitlist[i]]==12:
                return map[suitlist[i]]
            