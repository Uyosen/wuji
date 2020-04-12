import numpy as np


def double_t_maze():
    x = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
                  [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1], 
                  [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1], 
                  [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1], 
                  [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1], 
                  [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1], 
                  [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1], 
                  [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1], 
                  [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1], 
                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]], dtype=np.uint8)
    
    return x