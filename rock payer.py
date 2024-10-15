import math
guess = 1
i = 0
hortlist = []
hortthought = []
lengthcheck = 1
correctlist = []
hortinun = []
inputs = ['r','p','s','rock','paper','scissors']
while True:
    hortinun = []
    while hortinun not in inputs:
        hortinun = input('rock, paper or scissors: ')
        if hortinun in ['r','rock']:
            hortin = 0
        if hortinun in ['p','paper']:
            hortin = 1
        if hortinun in ['s','scissors']:
            hortin = 2
    hortlist.append(hortin)
    current = []
    print('the bot guessed',inputs[guess+3])
    if hortin == guess:
        print('the bot won')
        correctlist.append(0)
    elif guess == (hortin + 1)%3:
        print('the bot drew')
        correctlist.append(0)
    else:
        print('the bot lost')
        correctlist.append(1)
    print('the bot has been wrong',math.ceil(100*sum(correctlist)/len(correctlist)),'percent of the time')
    for i in range(len(hortlist)):

        current = hortlist[-lengthcheck:]

        for J in range(len(hortlist)- lengthcheck):
            checking = hortlist[J:J+lengthcheck]
            if checking == current:
                #dev
                #print('match')
                #print(current)
                #print(hortlist[0:J], '|', hortlist[J:J+lengthcheck], '|', hortlist[J+lengthcheck:len(hortlist)])
                #print(len(hortlist), J + lengthcheck)
                #print('append',hortlist[J + lengthcheck],pow((lengthcheck + math.ceil(J / 10)),2),'times')
                #end of dev
                for j in range(pow((lengthcheck + math.ceil((J/len(hortlist))*(lengthcheck/3))),2)):
                    hortthought.append(hortlist[J + lengthcheck])

        lengthcheck = lengthcheck + 1
    #dev 
    #print('list',hortthought)
    #end of dev
    #if not len(hortthought) == 0:
        #rawguess = sum(hortthought) / len(hortthought)
        #if rawguess > 0.5:
            #guess = 1
        #else:
           #guess = 0
    if not len(hortthought) == 0:
        rock = hortthought.count(0)
        paper = hortthought.count(1)
        scissors = hortthought.count(2)
        if rock >= paper and rock >= scissors:
            guess = 0
            #print('rock')
        elif paper >= scissors:
            guess = 1
            #print('paper')
        else:
            guess = 2
            #print('scissors')
            
    #dev
    #if guess == 0:
    #    print('the bot guessed heads with a confidence of')#,math.ceil(rawguess*100),'percent')
    #elif guess == 1:
    #    print('the bot guessed tails with a confidence of')#,math.ceil((1 - rawguess)*100),'percent')
    #else:
    #    print('the bot guessed tails with a confidence of')#,math.ceil((1 - rawguess)*100),'percent')
    #end of dev
    hortthought = []
    lengthcheck = 1
