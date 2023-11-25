import numpy as np
import game

def ucb_score(parent, child):

    prior_score = child.prior * np.sqrt(parent.visit_count) / (child.visit_count + 1)
    if child.visit_count > 0:
        value_score = -child.value()
    else:
        value_score = 0

    return value_score + prior_score



class Node:

    def __init__(self, prior, game_state, player):

        self.prior = prior
        self.player = player
        self.game_state = game_state
        self.visit_count = 0
        self.total_value = 0
        self.children = []

    def set_board(self, position):
        self.game_state = position

    def is_leave(self):
        if len(self.children) == 0:
            return True
        else:
            return False

    def value(self):
        if self.visit_count == 0:
            return 0
        return self.total_value / self.visit_count

    def get_visit_count_children(self):
        vc = []
        for c in self.children:
            vc.append(c.visit_count)

        return vc

    def get_total_value_children(self):
        tv = []
        for c in self.children:
            tv.append(c.total_value)

        return tv

    def get_ucb_score_children(self):
        ucb = []
        for c in self.children:
            ucb.append(ucb_score(self, c))
        return ucb

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
        if len(possible_moves) == 0:
            return False

        if prior_network == False:
            prior = np.ones(len(possible_moves))

        for i, move in enumerate(possible_moves):
            g_help = game.Game(self.mcts_game.get_board().copy())
            g_help.do_move(move)
            child = Node(prior[i], g_help.get_board(), node.player * -1)
            node.add_child(child)

    def mcts_rollout(self, node, player):
        self.mcts_game.set_board(node.game_state)
        winner = self.mcts_game.do_rollout(player)
        return winner

    def backpropagate(self, path, winner):

        update = self.root
        update.visit_count += 1
        update.total_value += winner * update.player
        for p in path:
            update = update.children[p]
            update.visit_count += 1
            update.total_value += winner * update.player



    def run(self, n_steps):
        for i in range(n_steps):
            path = []
            current = self.root
            while not current.is_leave():
                parent = current
                childs = current.children
                current = childs[0]
                add_path = 0
                for i, child in enumerate(childs):
                    if ucb_score(parent, child) > ucb_score(parent, current):
                        current = child
                        add_path = i

                path.append(add_path)


            self.expand(current)
            current = current.children[0]
            winner = self.mcts_rollout(current, current.player)


            self.backpropagate(path, winner)



if __name__ == '__main__':
    m = MCTS()
    m.root.set_board(np.array(
        [[0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]]
    ))
    m.run(500)
    print(m.root.get_visit_count_children())
    print(m.root.get_total_value_children())
    print(m.root.get_ucb_score_children())


