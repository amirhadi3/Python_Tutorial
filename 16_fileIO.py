# ----- FILE IO -----
# We can save and read data from files
# We start the code with with which guarantees
# the file will be closed if the program crashes
# mode w overwrites file
# mode a appends
with open("mydata.txt", mode="w", encoding="utf-8") \
        as myFile:
    # You can write to the file with write
    # It doesn't add a newline
    myFile.write("Some random text\nMore random text\nAnd some more")

# Open a file for reading
with open("mydata.txt", encoding="utf-8") as myFile:
    # Use read() to get everything at once
    print(myFile.read())

# you can also use open and close independently without "with"
print("\n\nanother read:")
myFile_0 = open("mydata.txt","r")
print(myFile_0.readable())
print(myFile_0.writable())
print(myFile_0.read(), "\n")
myFile_0.close()

# readlines
print("\n\nanother read:")
myFile_1 = open("mydata.txt","r")
print(myFile_1.readlines()[1], "\n")
myFile_1.close()

# Find out if the file is closed
print(myFile.closed)