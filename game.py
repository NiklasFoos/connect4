# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 22:07:17 2023

@author: Niklas Foos
"""

import numpy as np
import matplotlib.pyplot as plt


class Game:
    
    """
    This class contains everything for a game of connect 4.
    
    """
    
    
    def __init__(self):
        
        self.board = np.zeros((6,7))
        self.winner = 0
    
    
    def get_board(self):
        
        return self.board
    
    def get_winner(self):
        
        return self.winner
    
    def set_board(self, position):
        
        if position.shape == (6,7):        
            self.board = position
        else:
            print('this is not a valid position...')
    
    def move_possible(self, move):
        
        if self.board[5][move] == 0:
            return True
        else:
            return False
    
    def get_possible_moves(self):
        
        possible_moves = np.where(self.board[5] == 0)[0]
        return possible_moves
        
    def draw(self):
        
        if not self.gameOver() and np.all(self.board[5] != 0):
            return True
        else:
            return False
        
    def do_move(self, move):
        
        """
        Parameters
        -------------------
        move: number between 0 and 6 that denotes the column
        
        """
        
        if self.move_possible(move):          
            for row in range(6):
                if self.board[row][move] == 0:
                    self.board[row][move] = 1
                    self.board = -self.board
                    break
    
    def gameOver(self):
        
        # check rows:
        for row in range(6):
            for column in range(4):
                board_help = self.board[row, column:column+4]
                if abs(np.sum(board_help)) == 4:
                    self.winner = np.sign(board_help[0])
                    return True
                
                
        # check columns:
        for column in range(7):
            for row in range(3):
                board_help = self.board.T[column, row: row+4]
                if abs(np.sum(board_help)) == 4:
                    self.winner = np.sign(board_help[0])
                    return True
        
        # check diagonals:
        for row in range(3):
            for column in range(4):
                board_help = self.board[row:row+4,column:column+4]
                trace = np.trace(board_help)
                trace_off = np.trace(np.flip(board_help, 0))
                
                if abs(trace) == 4:
                    self.winner = np.sign(trace)
                    return True
                elif abs(trace_off) == 4:
                    self.winner = np.sign(trace_off)
                    return True

        return False
    
    def do_random_move(self):
        
        if self.draw():
            print('The game is draw')
            return self.board
        
        move = np.random.choice(self.get_possible_moves())
        
        self.do_move(move)
        
    def do_rollout(self):
        
        while not self.gameOver() and not self.draw():
            self.do_random_move()
            if self.gameOver() or self.draw():
                return self.board
        
    def show_board(self):

        
        ax = plt.axes()

        ax.set_facecolor('blue')
        colors = ['yellow' , 'red']
        for row in range(6):
            for column in range(7):
                if self.board[row][column] == 0:
                    continue
                else:
                    plt.scatter(column, row, color=colors[int((self.board[row][column] + 1)/2)], s = 800)
                
        plt.tick_params(left = False, right = False , labelleft = False , 
                labelbottom = False, bottom = False) 
        
        plt.xlim([-1, 7])
        plt.ylim([-1, 6])
        plt.show()
            
            
                
            
        
            
            
    
    
    
if __name__ == '__main__':
    
    draw = 0
    while draw == 0:
        g = Game()
        g.do_rollout()
        if g.draw():
            draw = 1
    
    g.show_board()
    print(g.draw())
    
    
    