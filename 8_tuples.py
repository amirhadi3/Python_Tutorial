# ----- TUPLES -----
# Tuples are just like lists except they are
# immutable
t1 = (1, 3.14, "Derek", False)

# Get length
print("Length ", len(t1))

# Get value / values
print("1st", t1[0])
print("Last", t1[-1])
print("1st 2", t1[0:2])
print("Every Other ", t1[0:-1:2])
print("Reverse ", t1[::-1])

# Everything you can do with lists you can do with
# tuples as long as you don't change values