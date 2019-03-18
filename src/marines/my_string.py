

def get_all_urls(line, start, urls):
    size = len(line)
    index = line.find("http://", start, size)
    endIndex = line.find(" ",index,size)
    endIndex = size if (endIndex == -1) else endIndex
    urls.append(line[index:endIndex])
    if ( endIndex == size):
        return urls
    else:
        return get_all_urls(line, endIndex, urls)


def get_urls(line=""):
    return get_all_urls(line, 0, [])


print get_urls("hi this is my site http://myfirst.site in facebook http://facebook.com/me twitter http://twitter/me my youtube: http://youtube/me")


##Write a function replace(s, old, new) that replaces all occurrences of old with new in a string s:
def replace(s, old, new):
    return s.replace(old, new);

print replace("hi every bohidy whihats wronghi", "hi", "")

def countLetters(line):
    letters = {}
    for i in range(len(line)):
        char = line[i].lower()
        if (char.isalpha()):
            if (char in letters):
                letters[char] = letters[char] + 1
            else:
                letters[char] = 1
    return sorted(letters.items())


print countLetters("ThiS is String with Upper and lower case Letters")
