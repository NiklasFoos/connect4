# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 22:07:17 2023

@author: Niklas Foos
"""

import numpy as np


class Game:
    
    """
    This class contains everything for a game of connect 4.
    
    """
    
    
    def __init__(self):
        
        self.board = np.zeros((6,7))
    
    
    def get_board(self):
        
        return self.board
    
    def move_possible(self, move):
        
        if self.board[5][move] == 0:
            return True
        else:
            print('this move is not possible')
            return False
        
    def do_move(self, move, player):
        
        """
        Parameters
        -------------------
        move: number between 0 and 6 that denotes the column
        player: 1 or -1 for eather of both players
        
        """
        
        if self.move_possible(move):          
            for row in range(6):
                if self.board[row][move] == 0:
                    self.board[row][move] = player
                    break
        
            
            
    
    
    
if __name__ == '__main__':
    
    g = Game()
    
    print(g.get_board())
    
    