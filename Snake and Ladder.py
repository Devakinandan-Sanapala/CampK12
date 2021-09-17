from random import randint

snake = [35,39,49,89,97,99]
snake_bite = [-30,-36,-15,-21,-11,-73]

ladder = [2,7,22,28,30,44,54,70,80,87]
ladder_climb = [21,22,19,49,2,14,15,20,3,6]

player1 = player2 = 0
turn = randint(1,2)

def rolldice():
    x = dice = randint (1,6)
    
    if x == 6:
        dice += rolldice()
    return dice

def snake_ladder(pos):
    if pos in snake:
        print("------snake bite------")
        return snake_bite[snake.index(pos)]
    
    elif pos in ladder:
        print("++++++ladder climb++++++")
        return ladder_climb[ladder.index(pos)]
    
    return 0

def add(pos,dice):
    if 100 - pos >= dice:
        return dice
    return 0


while player1<100 and player2<100:

    dice  = rolldice()
    
    if dice > 18:
        dice = 0
   
    if turn%2 == 0:
        print("player1 turn, at position =",player1," dice =",dice)
        player1 += add(player1,dice)
        player1 += snake_ladder(player1)

    else:
        print("player2 turn, at position =",player2," dice =",dice)
        player2 += add(player2,dice)
        player2 += snake_ladder(player2)

    turn += 1



if (player1 >= 100):
    print("Player 1 wins",player1)

else:
    print("Player 2 wins",player2)