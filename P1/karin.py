f = open(r"WEC-21\P3-WEC21\P1\Test1.txt", "r")

WORDS = []
i = 0

for x in f:
    WORDS.append(str.strip(x))

lowercase = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

time_value_dictionary = {
    "a": [0, 2],
    "b": [0.25, 2],
    "c": [0.5, 2],
    "d": 0,
    "e": 0.25,
    "f": 0.5,
    "g": 0,
    "h": 0.25,
    "i": 0.5,
    "j": 0,
    "k": 0.25,
    "l": 0.5,
    "m": 0,
    "n": 0.25,
    "o": 0.5,
    "p": 0,
    "q": 0.25,
    "r": 0.5,
    "s": 0.75,
    "t": 0,
    "u": 0.25,
    "v": 0.5,
    "w": 0,
    "x": 0.25,
    "y": 0.5,
    "z": 0.75,
    " ": 0,
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
    if word[i].isUpper():
        time += 2
    prev_letter = word[i - 1].lower()
    cur_letter = word[i].lower()
    # always add the same base time of the lowercase character
    time += time_value_dictionary.get(cur_letter)

    # check if you need to move to another button
    prev_key = time_value_dictionary.get(cur_letter[1])
