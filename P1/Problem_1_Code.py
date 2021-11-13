from timeit import default_timer as timer
start = timer()


def find_time(word):
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


def main():
    file = open(r"WEC-21\P3-WEC21\P1\Test1.txt", "r")
    words_solution = []
    min_time = -1

    for x in file:  # appending all the time values to array time
        time = find_time(str.strip(x))

        if min_time == -1:
            min_time = time[0]
            words_solution.append(time[1])
        elif min_time > time[0]:
            words_solution = []
            min_time = time[0]
            words_solution.append(time[1])
        elif min_time == time[0]:
            words_solution.append(time[1])

    print('Words with minimum time calculation:',
          (' '.join(map(str, words_solution))).replace(" ", ", "))
    print('Time calculation: ', min_time, 'seconds')
    return 0


if __name__ == "__main__":
    main()

end = timer()
print("Time taken: ", end - start)
