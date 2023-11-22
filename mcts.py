import numpy as np
def ucb_score(parent, child):

    if parent.visit_count == 0:
        return -np.inf

    else:
        prior_score = child.prior * np.sqrt(parent.visit_count) / (child.visit_count + 1)
        value_score = - child.total_value

    return value_score + prior_score



class Node:

    def __init__(self, prior):

        self.prior = prior
        self.visit_count = 0
        self.total_value = 0
        self.children = []


