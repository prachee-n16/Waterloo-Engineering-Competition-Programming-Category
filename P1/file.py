def time_Letter():
    return 0


def main():
    f = open(r"WEC-21\P3-WEC21\P1\Test1.txt", "r")
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
    WORDS = []
    i = 0

    for x in f:
        WORDS.append(str.strip(x))
        WORD = str.strip(x)

        for i in WORD:
            LETTER = str(i)
            print(time_value_dictionary.get(LETTER))

        print("\n")
