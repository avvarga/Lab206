import random
def coin_toss():
    heads = 0
    tails = 0
    for index in range(5000):
        toss = random.randint(0,1)
        if toss == 1:
            heads += 1
            print "Attempt #"+str(index)+": Throwing a coin... its a head! ... Got",heads,"head(s) so far and",tails,"so far"
        elif toss == 0:
            tails += 1
            print "Attempt #"+str(index)+": Throwing a coin... its a tail! ... Got",heads,"head(s) so far and",tails,"so far"
coin_toss()