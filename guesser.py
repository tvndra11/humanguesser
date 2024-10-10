import math
guess = 1
rawguess = 1
i = 0
hortlist = []
hortthought = []
lengthcheck = 1
while True:
    if guess == 1:
        hortinun = input('(h) heads (h) or tails (t): ')
    else:
        hortinun = input('(t) heads (h) or tails (t): ')
    if hortinun == 'h':
        hortin = 1
    else:
        hortin = 0
    hortlist.append(hortin)
    current = []
    if hortin == guess:
        print('the bot was correct')
    else:
        print('the bot was incorrect')
    for i in range(len(hortlist)):
        
        current = []
        for J in range(lengthcheck):
            current.append(hortlist[len(hortlist) - (lengthcheck - J)])
        for I in range(len(hortlist)):
            if current == hortlist[I:I+lengthcheck] and not I + lengthcheck == len(hortlist):
                #print('match')
                #print(current)
                #print(hortlist[0:I], '|', hortlist[I:I+lengthcheck], '|', hortlist[I+lengthcheck:len(hortlist)])
                #print(len(hortlist), I + lengthcheck)
                #print('append',hortlist[I + lengthcheck])
                hortthought.append(hortlist[I + lengthcheck])

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
