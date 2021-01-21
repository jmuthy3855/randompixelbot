import numpy as np
from PIL import Image

# Global vars
dead_count = 0 # used in boringCount
rows = 800
cols = 800

# generates the random cell auto and saves it
def genRandomCellAuto():
        global dead_count
        
        live_color = np.random.randint(30,255,3)
        imarray = genCellAuto(live_color, rows, cols)
        imarray = np.array(imarray).astype('uint8') 
        
        while isBoring(imarray):
            print("pattern is boring, regenerating")
            dead_count = 0
            imarray = genCellAuto(live_color, rows, cols) 
            imarray = np.array(imarray).astype('uint8') 

        im = Image.fromarray(imarray.astype('uint8')).convert('RGBA')
        im.save('resultimg.png')
        print("done with generating random pixels")


# randomly colors the live cells after they are generated, but looks like a mess in some cases
def randomColors(state):
    rows = len(state)
    cols = len(state[0])

    for i in range(0, rows):
       for j in range(0, cols):
           if state[i][j][0] != 0:
                state[i][j] = np.random.randint(0,255,3)

    return state

# will tell if a pattern is boring based on some arbitrary threshold
def isBoring(state):
    rows = len(state)
    cols = len(state[0])

    if dead_count < 0.1*rows*cols or dead_count > 0.9*rows*cols:
        return True
    else:
        return False

# initialize image and generate random rule using gen_rule
def genCellAuto(live_color, rows, cols):
    image_state = [[ live_color for j in range(0,cols)] for i in range(0,rows)]

    image_state[0][int(cols/2)] = [0, 0, 0]

    image_state = gen_rule(image_state, live_color) 

    return image_state
    
   


#generates a random rule, out of the 256 possible rule sets for an elementary ceullular automata
def gen_rule(state, live_color) :
    global dead_count
    num_rows = len(state)
    num_cols = len(state[0])
    
    random_rule = [live_color if np.random.randint(0,2) % 2 == 0 else [0,0,0] for i in range(0,8)]
    live_0 = live_color[0]
    rule_arr = [[[[0,0,0] for col in range(2)]for row in range(2)] for x in range(2)] 

    rule_arr[0][0][0] = random_rule[0] #4D array?!
    rule_arr[0][0][1] = random_rule[1]
    rule_arr[0][1][0] = random_rule[2]
    rule_arr[0][1][1] = random_rule[3]
    rule_arr[1][0][0] = random_rule[4]
    rule_arr[1][0][1] = random_rule[5]
    rule_arr[1][1][0] = random_rule[6]
    rule_arr[1][1][1] = random_rule[7]

    #ignoring corner cases, skip first row since that's gen 0
    for i in range (1,num_rows):
        for j in range(1, num_cols-1):
            left_cell = int(state[i-1][j-1][0] / live_0) #divide by live_0 so that these entries are either 0 or 1
            curr_cell = int(state[i-1][j][0] / live_0)
            right_cell = int(state[i-1][j+1][0] / live_0)

            #if confused, look at wolframalpha cellular automata
            #each of the 8 possibilities for left, curr, and right cells
            # state[i][j] = arr[left_cell][curr_cell][right_cell] will simply give the correct coloring..
            # so idea is you build this array once, then much faster updates as opposed to this if statement
            # state[i][j] = arr[0][0][0] -> maps to 000 pattern
            # state[i][j] = arr[0][0][1] -> maps to 001 pattern, etc.
            
            state[i][j] = rule_arr[left_cell][curr_cell][right_cell] 
            
            dead_count += int(state[i][j][0] / live_0) ^ 1 #add 1 if dead, else add 0
            
         
           

    return state


