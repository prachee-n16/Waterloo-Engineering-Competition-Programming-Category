f = open(r"C:\Users\prach\Desktop\ECE150\WEC-21\P3-WEC21\P1\Test1.txt", "r")

# Index for WORDS
i = 0
# Store the words in this array
WORDS = []
for x in f:
    # Store each word in the array!
    WORDS[i] = x
    i = i + 1
