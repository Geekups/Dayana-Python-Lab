import hashlib
import numpy as pynum_float
from time import sleep


with open('hash_list.txt', 'w') as f:
    for i in pynum_float.arange(0.00, 100.00, 0.01):
        hashed = hashlib.sha256(i)
        #print(hashed.hexdigest())
        
        f.write(f"\n {i} : {hashed.hexdigest()}")


break_point=0