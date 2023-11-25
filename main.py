import numpy as np
import game
import mcts

m = mcts.MCTS()

m.run(4)

print(m.root.get_visit_count_children())




