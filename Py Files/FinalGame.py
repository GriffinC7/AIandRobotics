#pip install "git+https://github.com/bblais/Game" --upgrade
from Robot373 import *
from classy import * 
from Game import *
from LeftTurn import leftturn
from RightTurn import rightturn
from DistForward import distbackward, distforward
from RobotGame import *

left,right=Motors("ab")
def stop():
    left.power=0
    right.power=0
    return

def random_move(state,player):    
    moves=valid_moves(state,player)
    return random.choice(moves)

random_agent=Agent(random_move) 
random_agent=Agent(random_move) 
def get_square(arr,index,shape,locations=None):
    import json
    
    if locations is None:
        with open('locations.json') as json_file:
            locations = json.load(json_file)        
    
    try:
        location=locations[index]
    except IndexError:
        print("locations.json file probably corrupt.")
        raise 
        
    c,r=location
    c1=int(c-shape[1]/2)
    c2=int(c+shape[1]/2)
    r1=int(r-shape[0]/2)
    r2=int(r+shape[0]/2)

    c2=c2+(shape[1]-(c2-c1))
    r2=r2+(shape[0]-(r2-r1))

    square=arr[r1:r2,c1:c2,:]
    
    return square
def read_state_from_file(filename='current_board.txt'):
    with open(filename) as fid:
        text=fid.read()

    text2=text.strip().split('\n')
    number_of_rows=len(text2)
    number_of_cols=len(text2[0].split())
    
    b=Board(number_of_rows,number_of_cols)
        
    board=[int(v) for v in text.split()]
    b.board=board
    return b

def read_state():
    from pylab import imread,imsave
    import os

    # train the classifier
    images=image.load_images('RotoPhotos2/squares/',delete_alpha=True)
    shape=images.data[0].shape[:2]
    data_train=data=image.images_to_vectors(images,verbose=True)  # train on all of them

    classifier=kNearestNeighbor()
    #classifier=NaiveBayes()
    classifier.fit(data_train.vectors,data_train.targets)


    # get the picture
    take_picture('current_board.jpg')
    arr=imread('current_board.jpg')


    # slice the picture into squares of the right size
    shape=data_train.shape[:2]
    squares=[get_square(arr,i,shape) for i in range(16)]
    test_images=image.array_to_image_struct(squares)

    # get predictions
    test_data=image.images_to_vectors(test_images)
    predictions=classifier.predict(test_data.vectors)

    if not os.path.exists('images/predicted'):
        os.mkdir('images/predicted')
    for i,(square,prediction) in enumerate(zip(squares,predictions)):
        imsave('images/predicted/ %d predicted as %s.jpg' % (i,data_train.target_names[prediction]),square)

    
    # reconstruct the state from the predictions
    state=Board(4,4)
    for i in range(16):
        color=data_train.target_names[predictions[i]]
        if color=="Nothing":
            state[i]=0
        elif color=="White":
            state[i]=1
        elif color=="Black":
            state[i]=2
        else:
            raise ValueError("You can't get there from here.")

    print("Current state is:")
    print(state)

    x=input("""
    Hit return if this is correct, otherwise type a character 
    and the state will be read from current_board.txt.""")

    if x:
        state=read_state_from_file()

    print("Using")
    print(state)
    return state

def get_move(state,player):
    if player==1:
        Q=LoadTable("Q1_agent_table1.json")
    else:
        Q=LoadTable("Q2_agent_table1.json")
        
    
    if state not in Q:
        return random_move(state,player)
    else:
        return top_choice(Q[state])
    
def make_move(move):
    print("Making move ",move)
    
    board=Board(4,4)  # just to get the conversion functions for free
    
    start,end=move
    rs,cs=board.rc_from_index(start)  # convert to row, column
    re,ce=board.rc_from_index(end)
    
    
    length_column=8.5
    length_row=6.5

    type_of_move=ce-cs  # 0 for a forward move, +1 for a right-hand diagonal, -1 for left-hand diagonal
    distance_to_column= length_column*(cs+1)
    distance_to_row=(4-rs)*length_row 

    if type_of_move==0:  # forward

        distforward(distance_to_column)
        stop()
        Wait(2)
        leftturn(4)
        stop()
        Wait(2)
        distforward(distance_to_row*2)
        Wait(2)
        distbackward(-(distance_to_row*2))
        stop()
        Wait(2)
        rightturn(4)
        stop()
        Wait(2)
        distbackward(-(distance_to_column))
        Wait(2)
        Shutdown()

    elif type_of_move==1:  # right-hand diagonal

        distforward(distance_to_column) #distance to column
        stop()
        Wait(2)
        leftturn(4)
        stop()
        Wait(2)
        distforward(distance_to_row) #distance to row
        stop()
        Wait(2)
        rightturn(13)
        stop()
        Wait(2)
        distforward(length_row) #stays
        stop()
        Wait(2)
        distbackward(-(length_row)) #stays
        stop()
        Wait(2)
        leftturn(13)
        stop()
        Wait(2)
        distbackward(-(distance_to_row)) #distance to row
        stop()
        Wait(2)
        rightturn(4)
        stop()
        Wait(2)
        distbackward(-(distance_to_column)) # disatnce to column
        Wait(2)

    elif type_of_move==-1:  # left-hand diagonal
        
        distforward(distance_to_column) #distance to column
        stop()
        Wait(2)
        leftturn(4)
        stop()
        Wait(2)
        distforward(distance_to_row) #distance to row
        stop()
        Wait(2)
        leftturn(13)
        stop()
        Wait(2)
        distforward(length_row) # stays
        stop()
        Wait(2)
        distbackward(-(length_row)) #stays
        stop()
        Wait(2)
        rightturn(13)
        stop()
        Wait(2)
        distbackward(-(distance_to_row)) #distance to row
        stop()
        Wait(2)
        rightturn(4)
        stop()
        Wait(2)
        distbackward(-(distance_to_column)) #distance to column
        Wait(2)

    else:
        raise ValueError("You can't get there from here.")


state = read_state()
move = get_move(state,2)
print(move)
Wait(3.0)
make_move(move)









