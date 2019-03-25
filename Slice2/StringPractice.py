
#link = https://www.youtube.com/watch?v=tqYAfUD7mQs
#print (link.find("youtube"))
def link (line, start, url):
    size = len(line)
    index = line.find("https://", start, size)
    endIndex = line.find(" ", index, size)
    endIndex = size if (endIndex == -1) else endIndex
    url.append(line[index:endIndex])
    return url if (endIndex == size) else get_all_urls(line, endIndex, urls)


def get_urls(line=""):
    return get_all_urls(line, 0, [])

##Write a function replace(s, old, new) that replaces all occurrences of old with new in a string s:
def replace(s, old, new):
    return s.replace(old, new).strip();
replace("Cochabamba", "a", "A") == "CochAbAmbA"



