# f = open(r"WEC-21\P3-WEC21\P1\Test1.txt", "r")

# WORDS = []
# i = 0

# for x in f:
#     WORDS.append(str.strip(x))

time_value_dictionary = {
    "a": [0, 2],
    "b": [0.25, 2],
    "c": [0.5, 2],
    "d": [0, 3],
    "e": [0.25, 3],
    "f": [0.5, 3],
    "g": [0, 4],
    "h": [0.25, 4],
    "i": [0.5, 4],
    "j": [0, 5],
    "k": [0.25, 5],
    "l": [0.5, 5],
    "m": [0, 6],
    "n": [0.25, 6],
    "o": [0.5, 6],
    "p": [0, 7],
    "q": [0.25, 7],
    "r": [0.5, 7],
    "s": [0.75, 7],
    "t": [0, 8],
    "u": [0.25, 8],
    "v": [0.5, 8],
    "w": [0, 9],
    "x": [0.25, 9],
    "y": [0.5, 9],
    "z": [0.75, 9],
    " ": [0, 0],
}

word = "heaVY"
time = 0

# iterate through the string
# count all upper case letters and the repeated letters
# turn the string to all lowercase
# compute extra
# use this information to do math to compute total time
for i in range(len(word)):
    # add extra time for uppercase chars
    print(word[i])
    if word[i].isupper():
        time += 2
    prev_letter = word[i - 1].lower()
    cur_letter = word[i].lower()
    # always add the same base time of the lowercase character
    time += time_value_dictionary.get(cur_letter[0])

    # check if you need to move to another button
    prev_key = time_value_dictionary.get(prev_letter[1])
    cur_key = time_value_dictionary.get(cur_letter[1])
    if prev_key == cur_key:
        time += 0.5
print("goodbye mars")
