from timeit import default_timer as timer

start = timer()
file = open(r"Part2.txt", "r")

WORDS = []
i = 0

# Key = character
# Value = [time value, number_key_associated]
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

min_time_words = []

# iterate through the string
# count all upper case letters and the repeated letters
# turn the string to all lowercase
# compute extra
# use this information to do math to compute total time


def find_time(word):

    time = 0
    for i in range(len(word)):
        # add extra time for uppercase chars
        if word[i].isupper():
            time += 2
        cur_letter = word[i].lower()
        if i == 0:
            time += time_value_dictionary.get(cur_letter)[0]

        else:
            prev_letter = word[i - 1].lower()
            # always add the same base time of the lowercase character
            time += time_value_dictionary.get(cur_letter)[0]

            # check if you need to move to another button
            prev_key = time_value_dictionary.get(prev_letter)[1]
            cur_key = time_value_dictionary.get(cur_letter)[1]

            if prev_key == cur_key:
                # the problem is, I dub
                time += 0.5
            else:
                time += 0.25
    return time, word


times_val = []
words = []

words_solution = []
first = True
broken_button = -1

for x in file:  # appending all the time values to array time
    # Fetch the broken button
    if first:
        broken_button = int(x)
        first = False
    else:
        time = find_time(str.strip(x))
        times_val.append(time[0])
        words.append(time[1])

min_time = times_val[0]
for i in range(len(times_val)):
    if times_val[i] < min_time:
        min_time = times_val[i]
        words_solution = []
        words_solution.append(words[i])
    elif times_val[i] == min_time:
        words_solution.append(words[i])

print(" ".join(map(str, words_solution)))
print(min_time, "seconds")


end = timer()
print("Time taken: ", end - start)
