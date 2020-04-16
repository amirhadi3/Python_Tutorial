# ----- SETS -----
# Sets are lists that are unordered, unique
# and while values can change those values
# must be immutable
s1 = set(["Derek", 1])
print("s1", s1)

s2 = {"Paul", 1}
print("s2", s2)

# Size
print("Length", len(s2))

# Join sets
s3 = s1 | s2
print(s3)

# Add value
s3.add("Doug")

# Remove value
s3.discard("Derek")

# Remove random value
print("Random", s3.pop())

# Add values in s2 to s3
s3 |= s2

# Return common values (You can include multiple
# sets as attributes)
print(s1.intersection(s2))

# All unique values
print(s1.symmetric_difference(s2))

# Values in s1 but not in s2
print(s1.difference(s2))

# Clear values
s3.clear()

# Frozen sets can't be edited
s4 = frozenset(["Paul", 7])
