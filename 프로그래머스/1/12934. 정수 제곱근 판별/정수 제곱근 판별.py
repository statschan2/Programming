def solution(n):
    import numpy as np
    if np.sqrt(n) % 1 == 0 : return (np.sqrt(n)+1)**2
    else : return -1