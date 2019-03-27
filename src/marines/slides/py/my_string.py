import re


def get_all_urls(line, start, urls):
    size = len(line)
    index = line.find("http://", start, size)
    endIndex = line.find(" ", index, size)
    endIndex = size if (endIndex == -1) else endIndex
    urls.append(line[index:endIndex])
    return urls if (endIndex == size) else get_all_urls(line, endIndex, urls)


def get_urls(line=""):
    return get_all_urls(line, 0, [])


##Write a function replace(s, old, new) that replaces all occurrences of old with new in a string s:
def replace(s, old, new):
    return s.replace(old, new).strip();


def countLetters(line):
    letters = {}
    for i in range(len(line)):
        char = line[i].lower()
        if (char.isalpha()):
            letters[char] = letters[char] + 1 if (char in letters) else 1
    return sorted(letters.items())


def match(regex, value):
    return value != None and bool(re.match(regex, value))


def is_valid_username(username):
    return match("[a-z0-9]", username)


def is_valid_password(password):
    return 8 <= len(password) <= 16 and match("[a-zA-Z0-9_]", password)


def is_valid_mail(email):
    return match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email)
