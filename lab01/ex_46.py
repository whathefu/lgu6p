import random, pprint

N = int(input("몇 게임? : "))


def lottery_game ():
    lottery = []

    # for i in range(6) :
    #     n =random.randrange(1,46)
        # if n != n :
        #     lottery.append(n)
        # # else :
        # #     del lottery[n]
        #     # lottery.append(n)



    while len(lottery) < 6 :
        n =random.randrange(1,46)
        if not (n in lottery) :
            lottery.append(n)

        # dup = False
        # for j in lottery:
        #     if n ==j:
        #         dup = True
        
        # if dup == False:
        #     lottery.append(n)
    return lottery

pprint.pprint(
    [lottery_game() for _ in range(N)],
    width=50
)


    # print(lottery)



