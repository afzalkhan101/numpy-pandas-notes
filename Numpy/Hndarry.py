import  numpy as np
import sys

s = range(100)
lst = list(s)
print(lst)
value = sys.getsizeof(s) * len(lst)
print("The value list size:",value)
