from random import randint
from objects import *
from tqdm import tqdm
import pandas as pd
import matplotlib.pyplot as plt
map = {'spades':'clubs' , 'clubs':'spades','hearts':'diamonds','diamonds':'hearts'}
iconmap = {'spades':'♠' , 'clubs':'♣','hearts':'♥','diamonds':'♦'}

#print("please input the suits count below")

occurdisplay={}

infodisplay={}

for ii in tqdm(range(10,-1,-1)):  #i=9
    for jj in range(10-ii,-1,-1):  # j=1,0
        for kk in range(10-ii-jj,-1,-1):   #k=1,0
            for hh in range(10-ii-jj-kk,-1,-1):  #h=0,1
                if  (ii>=jj and jj>=kk and kk>=hh and ii+jj+kk+hh==10):
                    spadecount=ii
                    clubcount=jj
                    diamondcount=kk
                    heartcount=hh
                    



# spadecount= int(input('spades♠:'))
# clubcount= int(input('clubs♣:'))
# diamondcount= int(input('diamonds♦:'))
# heartcount= int(input('hearts♥:'))


                    quanthand = {'spades':spadecount,'hearts':heartcount,'clubs':clubcount,'diamonds':diamondcount}  #sum is 10 if one hand info in 4 ways
                    displayhand = {'spades♠':quanthand['spades'],'hearts♥':quanthand['hearts'],'clubs♣':quanthand['clubs'],'diamonds♦':quanthand['diamonds']}
                    noOfCardInHand = sum(quanthand.values())


                    data_dict = {'♠':0,'♣':0,'♦':0,'♥':0}
                    rounds=100000

                    for i in tqdm(range(rounds)):
                        deck = Deck()
                        myhand = deck.cards[0:noOfCardInHand]
                        countmyhand = {'spades':0,'hearts':0,'diamonds':0,'clubs':0}
                        for item in myhand:
                            countmyhand[item] += 1

                        if countmyhand==quanthand:
                            result = deck.goalSuit()
                        else:
                            continue

                        if iconmap[result] in data_dict:
                            data_dict[iconmap[result]]+=1
                        else:
                            data_dict[iconmap[result]]=1

                    handss = ",".join(str(x) for x in [ii, jj, kk, hh])
                    totaloccurance = sum(data_dict.values())
                    if totaloccurance!=0:
                        distribution_dict = {k: format(v / totaloccurance, '.2f') for k, v in data_dict.items()}
                        top_2_suits = sorted(distribution_dict.items(), key=lambda x: x[1], reverse=True)[:2]
                        distribution_dict['Occurance'] = totaloccurance  
                        print("Combination: ",ii,jj,kk,hh, distribution_dict)
                        occurdisplay[handss]=distribution_dict['Occurance']

                        infotell = float(top_2_suits[0][1])    #the probi of the most likely suit
                        
                        infodisplay[handss]=infotell

                    else:
                        print("Combination: ",ii,jj,kk,hh,'  no occurance')
                        occurdisplay[handss]=0

df = pd.DataFrame(infodisplay, index = ['Info']).T  #can change to occurdisplay
#df = df/df.sum() #needed if occur
ax = df.sort_values(by='Info',ascending=False).plot(kind='bar')
#ax.set_xticklabels(ax.get_xticklabels(),rotation=0)
ax.bar_label(ax.containers[0]) # only 1 container needed unless using `hue`
plt.title(f"The information tell of each hand")
plt.show()