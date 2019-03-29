def countLetters(line):
    letters = {}
    for i in range(len(line)):
        char = line[i].lower()
        if (char.isalpha()):
            letters[char] = letters[char] + 1 if (char in letters) else 1
    return sorted(letters.items())