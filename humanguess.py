import math
guess = 1
rawguess = 1
i = 0
hortlist = []
hortthought = []
lengthcheck = 1
correctlist = []
while True:
    if guess == 1:
        hortinun = input('() heads (h) or tails (t): ')
    else:
        hortinun = input('() heads (h) or tails (t): ')
    if hortinun == 'h':
        hortin = 1
    else:
        hortin = 0
    hortlist.append(hortin)
    current = []
    if hortin == guess:
        print('the bot was correct')
        correctlist.append(1)
    else:
        print('the bot was incorrect')
        correctlist.append(0)
    print(sum(correctlist)/len(correctlist))
    for i in range(len(hortlist)):

        current = hortlist[-lengthcheck:]

        for J in range(len(hortlist)- lengthcheck):
            checking = hortlist[J:J+lengthcheck]
            if checking == current:
                #print('match')
                #print(current)
                #print(hortlist[0:J], '|', hortlist[J:J+lengthcheck], '|', hortlist[J+lengthcheck:len(hortlist)])
                #print(len(hortlist), J + lengthcheck)
                #print('append',hortlist[J + lengthcheck],pow((lengthcheck + math.ceil(J / 10)),2),'times')
                for j in range(pow((lengthcheck + math.ceil(J / 10)),2)):
                    hortthought.append(hortlist[J + lengthcheck])
        
        
        #for I in range(len(hortlist)):
            #if current == hortlist[I:I+lengthcheck] and not I + lengthcheck >= len(hortlist):
                #print('match')
                #print(current)
                #print(hortlist[0:I], '|', hortlist[I:I+lengthcheck], '|', hortlist[I+lengthcheck:len(hortlist)])
                #print(len(hortlist), I + lengthcheck)
                #print('append',hortlist[I + lengthcheck])
                #for j in range(pow(lengthcheck,2)):
                    #hortthought.append(hortlist[I + lengthcheck])

        lengthcheck = lengthcheck + 1
    #print('list',hortthought)
    if not len(hortthought) == 0:
        rawguess = sum(hortthought) / len(hortthought)
        if rawguess > 0.5:
            guess = 1
        else:
           guess = 0
    #print('guess',guess)
    hortthought = []
    lengthcheck = 1
