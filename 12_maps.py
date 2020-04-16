# ----- MAP -----
# Map is used to execute a function on a list
one_to_4 = range(1, 5)
times2 = lambda x: x * 2
print(list(map(times2, one_to_4)))