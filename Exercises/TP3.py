import random
import time
import numpy as np
from copy import deepcopy

NUM_ROWS = 6
NUM_COLS = 7

class State:
    
    def __init__(self):
        # initialize the board info here and any additional variables
        self.board = np.zeros((NUM_ROWS, NUM_COLS)) # board initial state (all zeros)
        self.column_heights = [NUM_ROWS - 1] * NUM_COLS # useful to keep track of the index in which pieces should be inserted
        self.available_moves = list(range(7)) # list of playable columns (not full)
        self.player = 1
        self.winner = -1 # -1 - no winner (during game); 0 - draw; 1- player 1; 2 - player 2
        
    def move(self, column): 
        # function that performs a move given the column number and returns the new state
        # do not forget to update the available moves list, column heights, pass the turn and check for winners
        state_copy = deepcopy(self)
        
        height = state_copy.column_heights[column]
        state_copy.column_heights[column] = height
        state_copy.board[height][column] = self.player
        
        if height == 0:
            state_copy.available_moves.remove(column)
        else:
            state_copy.column_heights[column] = height - 1
        
        state_copy.update_winner() 
        state_copy.player = 3 - self.player # update player turn
        
        return state_copy
    
    def update_winner(self):
        # function that tests objective and update the winner accordingly
        # sholud return 1, 2 or 0 (draw)
        # Your Code Here
        pass

    
    def check_line(self, n, player, values):
        num_pieces = sum(list(map(lambda val: val == player, values)))
        if n == 4:
            return num_pieces == 4
        if n == 3:
            num_empty_spaces = sum(list(map(lambda val: val == 0, values)))
            return num_pieces == 3 and num_empty_spaces == 1
    
    # c1) c2)
    def count_lines(self, n, player):
        num_lines = 0
        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                if col < NUM_COLS - 3 and self.check_line(n, player, [self.board[row][col], self.board[row][col+1], self.board[row][col+2], self.board[row][col+3]]):
                    num_lines += 1
                if row < NUM_ROWS - 3 and self.check_line(n, player, [self.board[row][col], self.board[row+1][col], self.board[row+2][col], self.board[row+3][col]]):
                    num_lines += 1
                 # Your Code Here
        return num_lines
    
    # c3)
    def central(self, player):
        # Your Code Here
        pass

class ConnectFourGame:
    
    def __init__(self, player_1_ai, player_2_ai):
        self.state = State()
        self.player_1_ai = player_1_ai
        self.player_2_ai = player_2_ai
        
    def start(self, log_moves = False):
        self.state = State()
        while True:
            if self.state.player == 1:
                self.player_1_ai(self)
            else:
                self.player_2_ai(self)
            
            if log_moves:
                print(game.state.board)
            
            if self.state.winner != -1:
                break
        
        if self.state.winner == 0:
            print("End of game! Draw!")
        else:
            print(f"End of game! Player {self.state.winner} wins!")
    
    def run_n_matches(self, n, max_time = 3600, log_moves = False):
        start_time = time.time()
        
        results = [0, 0, 0] # [draws, player 1 victories, player 2 victories]
        
        # Your Code Here
     
        print("\n=== Elapsed time: %s seconds ===" % (int(time.time() - start_time)))
        print(f"  Player 1: {results[1]} victories")
        print(f"  Player 2: {results[2]} victories")
        print(f"  Draws: {results[0]} ")
        print("===============================")
               
""" 
    Heuristic functions - e)
"""

def evaluate_f1(state):
    return state.count_lines(4, 1) - state.count_lines(4, 2)

def evaluate_f2(state):
    return (state.count_lines(4, 1) - state.count_lines(4, 2)) * 100 + state.count_lines(3, 1) - state.count_lines(3, 2)

def evaluate_f3(state):
    return 100 * evaluate_f1(state) + state.central(1) - state.central(2)

def evaluate_f4(state):
    return 5 * evaluate_f2(state) + evaluate_f3(state)     

""" 
    Move selection methods
"""
    
def execute_random_move(game):
    move = random.choice(game.state.available_moves)
    game.state = game.state.move(move)
    
def execute_minimax_move(evaluate_func, depth):
    pass

def minimax(state, depth, alpha, beta, maximizing, player, evaluate_func):
    pass
