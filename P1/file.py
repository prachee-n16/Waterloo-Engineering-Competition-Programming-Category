def time_Word(word):
    time_value_dictionary = {"a": 0,
                             "b": 0.25,
                             "c": 0.5,
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
    word = "Crisp"
    time = 0

    for i in range(len(word)):
        # add extra time for uppercase chars
        print(word[i])
        if word[i].isupper():
            time += 2

        if i != 0:
            prev_letter = word[i - 1].lower()
            cur_letter = word[i].lower()
            # always add the same base time of the lowercase character
            time += time_value_dictionary.get(cur_letter)[0]

            # check if you need to move to another button
            prev_key = time_value_dictionary.get(prev_letter)[1]
            cur_key = time_value_dictionary.get(cur_letter)[1]
            print("prev key" + str(prev_key))
            print("cur key" + str(cur_key))
            if prev_key == cur_key:
                # the problem is, I dub
                time += 0.5
            else:
                time += 0.25
    print(time)


if __name__ == "__main__":
    # Open the file
    f = open(r"WEC-21\P3-WEC21\P1\Test1.txt", "r")

    # For each word in this file
    for x in f:
        # Strip EOL character
        word = str.strip(x)
        # Function call to determine time in letter
        # time_Word(WORD)
        time_Word("dEFi")
