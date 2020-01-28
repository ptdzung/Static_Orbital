#
# CS1010S --- Programming Methodology
#
# Sidequest 10.1 Template
#
# Note that written answers are commented out to allow us to run your #
# code easily while grading your problem set.

from random import *
from puzzle import GameGrid

###########
# Helpers #
###########

def accumulate(fn, initial, seq):
    if not seq:
        return initial
    else:
        return fn(seq[0],
                  accumulate(fn, initial, seq[1:]))

def flatten(mat):
    return [num for row in mat for num in row]



###########
# Task 1  #
###########

def new_game_matrix(n):
    return [[0] * n for row in range(n)]

def has_zero(mat):
    return 0 in flatten(mat)

def add_two(mat):
    nrow = len(mat)
    ncol = len(mat[0])
    list_zeros = []
    for i in range(nrow):
        for j in range(ncol):
            if mat[i][j] == 0:
                list_zeros.append((i, j))
    k = randint(0, len(list_zeros) - 1)
    (i, j) = list_zeros[k]
    mat[i][j] = 2
    return mat
    
print(add_two(new_game_matrix(3)))

###########
# Task 2  #
###########

def game_status(mat):
    def same_adjacent(mat):
        nrow = len(mat)
        ncol = len(mat[0])
        for i in range(nrow - 1):
            for j in range(ncol - 1):
                if mat[i][j] == mat[i+1][j] or mat[i][j] == mat[i][j+1]:
                    return True
        return False
    nrow = len(mat)
    ncol = len(mat[0])           
    flat = flatten(mat)
    if 2048 in flat:
        return "win"
    if same_adjacent(mat) == True:
        return "not over"
    if 0 in flat:
        return "not over"
    else:
        return "lose"



###########
# Task 3a #
###########

def transpose(mat):
    result = []
    nrow = len(mat)
    ncol = len(mat[0])
    for i in range(nrow):
        for j in range(ncol):
            if len(result) <= j:
                result.append([mat[i][j]])
            else:
                result[j].append(mat[i][j])
    return result

###########
# Task 3b #
###########

def reverse(mat):
    reverse_mat = []
    nrow = len(mat)
    ncol = len(mat[0])
    for row in mat:
        new_row = []
        for i in range(ncol):
            new_row.append(row[ncol - i - 1])
        reverse_mat.append(new_row)
    return reverse_mat

print(reverse([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))

############
# Task 3ci #
############

def merge_left(mat):
    nrow = len(mat)
    ncol = len(mat[0])
    new_mat = []
    score_increment = 0
    def get_leftmost_available(row):
        list_of_zeros = []
        for i in range(len(row)):
            if row[i] == 0:
                list_of_zeros.append(i)
        if list_of_zeros != []:
            return int(min(list_of_zeros))
        else:
            return -1
    for row in mat:
        for i in range(ncol):
            a = get_leftmost_available(row[:i])
            if row[i:] == [0] * (ncol - i - 1) or i == ncol - 1:
                if a == -1:
                    pass
                else:
                    row[a] += row[i]
                    row[i] = 0
                    break
            elif row[i] == row[i + 1]:
                if a == -1:
                    row[i] *= 2
                    row[i + 1] = 0
                    score_increment += row[i]
                else:
                    score_increment += row[i] * 2
                    row[a] = row[i] + row[i + 1]
                    row[i] = 0
                    row[i + 1] = 0
            else:
                if a == -1:
                    pass
                else:
                    row[a] += row[i]
                    row[i] = 0
        new_mat.append(row)
    return (new_mat,  new_mat == mat, score_increment)


#############
# Task 3cii #
#############

def merge_right(mat):
    return reverse(merge_left(reverse(mat)))

def merge_up(mat):
    return transpose(merge_left(transpose(mat)))

def merge_down(mat):
    return transpose(merge_right(reverse(transpose(mat))))


###########
# Task 3d #
###########

def text_play():
    def print_game(mat, score):
        for row in mat:
            print(''.join(map(lambda x: str(x).rjust(5), row)))
        print('score: ' + str(score))
    GRID_SIZE = 4
    score = 0
    mat = add_two(add_two(new_game_matrix(GRID_SIZE)))
    print_game(mat, score)
    while True:
        move = input('Enter W, A, S, D or Q: ')
        move = move.lower()
        if move not in ('w', 'a', 's', 'd', 'q'):
            print('Invalid input!')
            continue
        if move == 'q':
            print('Quitting game.')
            return
        move_funct = {'w': merge_up,
                      'a': merge_left,
                      's': merge_down,
                      'd': merge_right}[move]
        mat, valid, score_increment = move_funct(mat)
        if not valid:
            print('Move invalid!')
            continue
        score += score_increment
        mat = add_two(mat)
        print_game(mat, score)
        status = game_status(mat)
        if status == "win":
            print("Congratulations! You've won!")
            return
        elif status == "lose":
            print("Game over. Try again!")
            return

# UNCOMMENT THE FOLLOWING LINE TO TEST YOUR GAME
text_play()


# How would you test that the winning condition works?
# Your answer:
#


##########
# Task 4 #
##########

def make_state(matrix, total_score):
    return (matrix, total_score)

def get_matrix(state):
    return state[0]

def get_score(state):
    return state[1]

def make_new_game(n):
    return add_two(new_game_matrix(n))

def left(state):
    matrix = get_matrix(state)
    new_matrix = merge_left(matrix)
    new_state = make_state(new_matrix[0], new_matrix[2])
    boolean = new_matrix[1]
    return new_state, boolean

def right(state):
    matrix = get_matrix(state)
    new_matrix = merge_right(matrix)
    new_state = make_state(new_matrix[0], new_matrix[2])
    boolean = new_matrix[1]
    return new_state, boolean

def up(state):
    matrix = get_matrix(state)
    new_matrix = merge_up(matrix)
    new_state = make_state(new_matrix[0], new_matrix[2])
    boolean = new_matrix[1]
    return new_state, boolean

def down(state):
    matrix = get_matrix(state)
    new_matrix = merge_down(matrix)
    new_state = make_state(new_matrix[0], new_matrix[2])
    boolean = new_matrix[1]
    return new_state, boolean


# Do not edit this #
game_logic = {
    'make_new_game': make_new_game,
    'game_status': game_status,
    'get_score': get_score,
    'get_matrix': get_matrix,
    'up': up,
    'down': down,
    'left': left,
    'right': right,
    'undo': lambda state: (state, False)
}

# UNCOMMENT THE FOLLOWING LINE TO START THE GAME (WITHOUT UNDO)
#gamegrid = GameGrid(game_logic)




#################
# Optional Task #
#################

###########
# Task 5i #
###########

def make_new_record(mat, increment):
    "Your answer here"

def get_record_matrix(record):
    "Your answer here"

def get_record_increment(record):
    "Your answer here"

############
# Task 5ii #
############

def make_new_records():
    "Your answer here"

def push_record(new_record, stack_of_records):
    "Your answer here"

def is_empty(stack_of_records):
    "Your answer here"

def pop_record(stack_of_records):
    "Your answer here"

#############
# Task 5iii #
#############

# COPY AND UPDATE YOUR FUNCTIONS HERE
def make_state(matrix, total_score, records):
    "Your answer here"

def get_matrix(state):
    "Your answer here"

def get_score(state):
    "Your answer here"

def make_new_game(n):
    "Your answer here"

def left(state):
    "Your answer here"

def right(state):
    "Your answer here"

def up(state):
    "Your answer here"

def down(state):
    "Your answer here"

# NEW FUNCTIONS TO DEFINE
def get_records(state):
    "Your answer here"

def undo(state):
    "Your answer here"


# UNCOMMENT THE FOLLOWING LINES TO START THE GAME (WITH UNDO)
##game_logic = {
##    'make_new_game': make_new_game,
##    'game_status': game_status,
##    'get_score': get_score,
##    'get_matrix': get_matrix,
##    'up': up,
##    'down': down,
##    'left': left,
##    'right': right,
##    'undo': undo
##}
#gamegrid = GameGrid(game_logic)
