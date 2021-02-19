import numpy as np

map_matrix = {} # maybe the map should be an object. also find out of there is way to avoid using global keyword

def init_map(num_rows, num_cols):
    global map_matrix
    map_matrix = [[0 for j in range(num_cols)] for i in range(num_rows)]

def print_map():
    """
    print map in general matrix, or row-col form
    """
    global map_matrix
    for i in range(len(map_matrix)):
        for j in range(len(map_matrix[0])):
            print(map_matrix[i][j], end=' ')
        print("\n")


def dfs(start_row, start_col):
    """
    generate random path through map
    random chooses to go right or down, and continues until the bottom or right side of the map is reached
    a 1 indicates the direction taken at that cell is right
    a 2 indicates the direction taken at that cell is down
    a 3 indicates the end of the path
    """
    global map_matrix
    
    direction = np.random.randint(0, 2)
    
    if direction == 0 and start_col < len(map_matrix[0]) - 1:
        map_matrix[start_row][start_col] = 1
        dfs(start_row, start_col + 1)
    elif start_row < len(map_matrix) - 1:
        map_matrix[start_row][start_col] = 2
        dfs(start_row + 1, start_col)
    else:
        map_matrix[start_row][start_col] = 3


    return

def main():
    init_map(10, 10)
    dfs(0,0)
    print_map()


if __name__ == '__main__':
    main()