# ----- DICTIONARIES -----
# Dictionaries are lists of key / value pairs
# Keys and values can use any data type
# Duplicate keys aren't allowed
heroes = {
    "Superman": "Clark Kent",
    "Batman": "Bruce Wayne"
}

villains = dict([
    ("Lex Luthor", "Lex Luthor"),
    ("Loki", "Loki")
])

print("Length", len(heroes))

# Get value by key
# Also heroes.get("Superman")
print(heroes["Superman"])

# Add more
heroes["Flash"] = "Barry Allan"

# Change a value
heroes["Flash"] = "Barry Allen"

# Get list of tuples
print(list(heroes.items()))

# Get list of keys and values
print(list(heroes.keys()))
print(list(heroes.values()))

# Delete
del heroes["Flash"]

# Remove a key and return it
print(heroes.pop("Batman"))

# Search for key
print("Superman" in heroes)

# Cycle through a dictionary
for k in heroes:
    print(k)

for v in heroes.values():
    print(v)

# Formatted print with dictionary mapping
d1 = {"name": "Bread", "price": .88}
print("%(name)s costs $%(price).2f" % d1)