import numpy as np
from PIL import Image

# global vars
dead_count = 0 # used in boring_count, probably can change to a non-global variable that is returned in 
rows = 800
cols = 800

# generates the random cell auto and saves it in the specified save file, which should be a valid photo file type
def gen_random_cellauto(save_file):
        live_color = np.random.randint(30,255,3)
        imarray = img_gen(live_color, rows, cols)
         
        while is_boring(imarray):
            print("pattern is boring, regenerating")
            imarray = img_gen(live_color, rows, cols)  

        im = Image.fromarray(imarray.astype('uint8')).convert('RGBA')
        im.save(save_file)
        print("done with generating random pixels, saved in {}".format(save_file))

# generates 5 random cellautos, saves them into different files
def gen_multiple_cellauto():
    save_file = 'multipleresultimg{}.png'

    for i in range(0, 5):
        gen_random_cellauto(save_file.format(i))


# randomly colors the live cells after they are generated, but looks like a mess in some cases
def random_colors(state):
    rows = len(state)
    cols = len(state[0])

    for i in range(0, rows):
       for j in range(0, cols):
           if state[i][j][0] != 0:
                state[i][j] = np.random.randint(0,255,3) # try doing this branchless! might not help though...

    return state

# will tell if a pattern is boring based on some arbitrary threshold
def is_boring(state):
    if dead_count < 0.13*rows*cols or dead_count > 0.87*rows*cols:
        return True
    else:
        return False

# initialize image and generate random rule using gen_rule
def img_gen(live_color, rows, cols):
    image_state = [[ live_color for j in range(0,cols)] for i in range(0,rows)]
    image_state[0][int(cols / 2)] = [0, 0, 0]

    image_state = gen_rule(image_state, live_color)
    image_state = np.array(image_state).astype('uint8')

    return image_state

# generate random rule for gen_rule out of the 256 possible rule sets for an elementary ceullular automata. only one line but could change if generating randome rule becomes more complicated later
def random_rule(live_color):
    return [[[live_color if np.random.randint(0,2) % 2 == 0 else [0,0,0] for right in range(2)] for curr in range(2)] for left in range(2)]
    
# generates a random rule and creates cellauto img state 
def gen_rule(state, live_color) :
    global dead_count
    dead_count = 0 # assume there are no dead cells in the beginning
    
    rule_arr = random_rule(live_color)

    # ignoring corner cases, skip first row since that's gen 0, come back to corner cases sometime
    for i in range (1, rows):
        for j in range(1, cols - 1):
            left_cell = int(state[i - 1][j - 1][0] / live_color[0]) # divide by live_0 so that these entries are either 0 or 1, basically tells whether cell is dead or not
            curr_cell = int(state[i - 1][j][0] / live_color[0])
            right_cell = int(state[i - 1][j + 1][0] / live_color[0])

            # if confused, look at wolframalpha cellular automata
            # each of the 8 possibilities for left, curr, and right cells
            # state[i][j] = arr[left_cell][curr_cell][right_cell] will simply give the correct coloring..
            # so idea is you build this array once, then faster updates to the image state as opposed to if statements
            # state[i][j] = arr[0][0][0] -> maps to 000 pattern
            # state[i][j] = arr[0][0][1] -> maps to 001 pattern, etc.
            
            state[i][j] = rule_arr[left_cell][curr_cell][right_cell] 
            
            dead_count += int(state[i][j][0] / live_color[0]) ^ 1 #add 1 if dead, else add 0
        
    return state



