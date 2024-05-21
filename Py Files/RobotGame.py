from Game import *


def initial_state():
    state=Board(4,4)
    state[0] = 1
    state[1] = 1
    state[2] = 1
    state[3] = 1
    state[12] = 2
    state[13] = 2
    state[14] = 2
    state[15] = 2
    return state



#valid moves 
def valid_moves(state,player):
    emptySquare = 0
    player1 = 1
    player2 = 2
    
    moves = []
    if player== 1:
        if state[0] == 1 and state[4]== 0:
            moves.append([0,4])
        if state[1] == 1 and state[5]== 0:
            moves.append([1,5])
        if state[2] == 1 and state[6]== 0:
            moves.append([2,6])
        if state[3] == 1 and state[7]== 0:
            moves.append([3,7])    
        if state[4] == 1 and state[8]== 0:
            moves.append([4,8])
        if state[5] == 1 and state[9]== 0:
            moves.append([5,9])
        if state[6] == 1 and state[10]== 0:
            moves.append([6,10])
        if state[7] == 1 and state[11]== 0:
            moves.append([7,11])
        if state[8] == 1 and state[12]== 0:
            moves.append([8,12])
        if state[9] == 1 and state[13]== 0:
            moves.append([9,13])
        if state[10] == 1 and state[14]== 0:
            moves.append([10,14])
        if state[11] == 1 and state[15]== 0:
            moves.append([11,15])

        if state[0] == 1 and state[5]== 0:
            moves.append([0,5])
        if state[1] == 1 and state[4]== 0:
            moves.append([1,4])
        if state[1] == 1 and state[6]== 0:
            moves.append([1,6])
        if state[2] == 1 and state[5]== 0:
            moves.append([2,5])
        if state[2] == 1 and state[7]== 0:
            moves.append([2,7])
        if state[3] == 1 and state[6]== 0:
            moves.append([3,6])

        if state[4] == 1 and state[9]== 0:
            moves.append([4,9])
        if state[5] == 1 and state[8]== 0:
            moves.append([5,8])
        if state[5] == 1 and state[10]== 0:
            moves.append([5,10])
        if state[6] == 1 and state[9]== 0:
            moves.append([6,9])
        if state[6] == 1 and state[11]== 0:
            moves.append([6,11])
        if state[7] == 1 and state[10]== 0:
            moves.append([7,10])

        if state[8] == 1 and state[13]== 0:
            moves.append([8,13])
        if state[9] == 1 and state[12]== 0:
            moves.append([9,12])
        if state[9] == 1 and state[14]== 0:
            moves.append([9,14])
        if state[10] == 1 and state[13]== 0:
            moves.append([10,13])
        if state[10] == 1 and state[15]== 0:
            moves.append([10,15])
        if state[11] == 1 and state[14]== 0:
            moves.append([11,14])

        if state[0] == 1 and state[5]== 2:
            moves.append([0,5])
        if state[1] == 1 and state[4]== 2:
            moves.append([1,4])
        if state[1] == 1 and state[6]== 2:
            moves.append([1,6])
        if state[2] == 1 and state[5]== 2:
            moves.append([2,5])
        if state[2] == 1 and state[7]== 2:
            moves.append([2,7])
        if state[3] == 1 and state[6]== 2:
            moves.append([3,6])

        if state[4] == 1 and state[9]== 2:
            moves.append([4,9])
        if state[5] == 1 and state[8]== 2:
            moves.append([5,8])
        if state[5] == 1 and state[10]== 2:
            moves.append([5,10])
        if state[6] == 1 and state[9]== 2:
            moves.append([6,9])
        if state[6] == 1 and state[11]== 2:
            moves.append([6,11])
        if state[7] == 1 and state[10]== 2:
            moves.append([7,10])

        if state[8] == 1 and state[13]== 2:
            moves.append([8,13])
        if state[9] == 1 and state[12]== 2:
            moves.append([9,12])
        if state[9] == 1 and state[14]== 2:
            moves.append([9,14])
        if state[10] == 1 and state[13]== 2:
            moves.append([10,13])
        if state[10] == 1 and state[15]== 2:
            moves.append([10,15])
        if state[11] == 1 and state[14]== 2:
            moves.append([11,14])

    if player== 2:
        if state[12] == 2 and state[8]== 0:
            moves.append([12,8])
        if state[13] == 2 and state[9]== 0:
            moves.append([13,9])
        if state[14] == 2 and state[10]== 0:
            moves.append([14,10])
        if state[15] == 2 and state[11]== 0:
            moves.append([15,11])    
        if state[8] == 2 and state[4]== 0:
            moves.append([8,4])
        if state[9] == 2 and state[5]== 0:
            moves.append([9,5])
        if state[10] == 2 and state[6]== 0:
            moves.append([10,6])
        if state[11] == 2 and state[7]== 0:
            moves.append([11,7])
        if state[4] == 2 and state[0]== 0:
            moves.append([4,0])
        if state[5] == 2 and state[1]== 0:
            moves.append([5,1])
        if state[6] == 2 and state[2]== 0:
            moves.append([6,2])
        if state[7] == 2 and state[3]== 0:
            moves.append([7,3])

        if state[12] == 2 and state[9]== 0:
            moves.append([12,9])
        if state[13] == 2 and state[8]== 0:
            moves.append([13,8])
        if state[13] == 2 and state[10]== 0:
            moves.append([13,10])
        if state[14] == 2 and state[9]== 0:
            moves.append([14,9])
        if state[14] == 2 and state[11]== 0:
            moves.append([14,11])
        if state[15] == 2 and state[10]== 0:
            moves.append([15,10])

        if state[8] == 2 and state[5]== 0:
            moves.append([8,5])
        if state[9] == 2 and state[4]== 0:
            moves.append([9,4])
        if state[9] == 2 and state[6]== 0:
            moves.append([9,6])
        if state[10] == 2 and state[5]== 0:
            moves.append([10,5])
        if state[10] == 2 and state[7]== 0:
            moves.append([10,7])
        if state[11] == 2 and state[6]== 0:
            moves.append([11,6])

        if state[4] == 2 and state[1]== 0:
            moves.append([4,1])
        if state[5] == 2 and state[0]== 0:
            moves.append([5,0])
        if state[5] == 2 and state[2]== 0:
            moves.append([5,2])
        if state[6] == 2 and state[1]== 0:
            moves.append([6,1])
        if state[6] == 2 and state[3]== 0:
            moves.append([6,3])
        if state[7] == 2 and state[2]== 0:
            moves.append([7,2])

        if state[12] == 2 and state[9]== 1:
            moves.append([12,9])
        if state[13] == 2 and state[8]== 1:
            moves.append([13,8])
        if state[13] == 2 and state[10]== 1:
            moves.append([13,10])
        if state[14] == 2 and state[9]== 1:
            moves.append([14,9])
        if state[14] == 2 and state[11]== 1:
            moves.append([14,11])
        if state[15] == 2 and state[10]== 1:
            moves.append([15,10])

        if state[8] == 2 and state[5]== 1:
            moves.append([8,5])
        if state[9] == 2 and state[4]== 1:
            moves.append([9,4])
        if state[9] == 2 and state[6]== 1:
            moves.append([9,6])
        if state[10] == 2 and state[5]== 1:
            moves.append([10,5])
        if state[10] == 2 and state[7]== 1:
            moves.append([10,7])
        if state[11] == 2 and state[6]== 1:
            moves.append([11,6])

        if state[4] == 2 and state[1]== 1:
            moves.append([4,1])
        if state[5] == 2 and state[0]== 1:
            moves.append([5,0])
        if state[5] == 2 and state[2]== 1:
            moves.append([5,2])
        if state[6] == 2 and state[1]== 1:
            moves.append([6,1])
        if state[6] == 2 and state[3]== 1:
            moves.append([6,3])
        if state[7] == 2 and state[2]== 1:
            moves.append([7,2])
            
    return moves

def update_state(state,player,move):
    new_state=state
    start,end = move
    new_state[start]=0
    new_state[end] = player
    
    return new_state

def show_state(state):
    print(state)
    
def win_status(state,player):
#if there are no possible moves for player2, player1 wins
#if there are no possible moves for player1, player2 wins
#no way you can lose on your turn
# no stalemate
    if player==1:
        player=2
    else:
        player=1        
    if state[0] == 2:
        return 'win'
    if state[1] == 2:
        return 'win'
    if state[2] == 2:
        return 'win'
    if state[3] == 2:
        return 'win'
    if state[12] == 1:
        return 'win'
    if state[13] == 1:
        return 'win'
    if state[14] == 1:
        return 'win'
    if state[15] == 1:
        return 'win'
    if not valid_moves(state,player):
        return 'win'
    #if not valid_moves(state,player):
        #return 'win'


    