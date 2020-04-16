from functools import reduce
# ----- REDUCE -----
# Reduce receives a list and returns a single
# result
# Add up the values in a list
print(reduce((lambda x, y: x + y), range(1, 6)))