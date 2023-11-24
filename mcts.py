import numpy as np
import game

def ucb_score(parent, child):

    prior_score = child.prior * np.sqrt(parent.visit_count) / (child.visit_count + 1)
    value_score = - child.total_value

    return value_score + prior_score



class Node:

    def __init__(self, prior, game_state, player):

        self.prior = prior
        self.player = player
        self.game_state = game_state
        self.visit_count = 0
        self.total_value = 0
        self.children = []


    def get_children(self):
        return self.children

    def add_child(self, node):
        self.children.append(node)


class MCTS:

    def __init__(self):

        self.mcts_game = game.Game()
        self.root = Node(1, self.mcts_game.get_board().copy(), 1)

    def get_root(self):
        return self.root

    def expand(self, node, prior_network = False):
        state = node.game_state
        self.mcts_game.set_board(state)
        possible_moves = self.mcts_game.get_possible_moves()
        if prior_network == False:
            prior = 1/len(possible_moves) * np.ones(len(possible_moves))

        for i, move in enumerate(possible_moves):
            g_help = game.Game(self.mcts_game.get_board().copy())
            g_help.do_move(move)
            child = Node(prior[i], g_help.get_board(), node.player * -1)
            node.add_child(child)



