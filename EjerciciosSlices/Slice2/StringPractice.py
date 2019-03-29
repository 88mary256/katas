
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



# Function 1, Slice 3:
def mi_lista(number):
nro= input("Inserte el nro de elementos en la lista: ")
for nro in range (len(List)):
        id = int(List[i])
        if (1 <= id <= 100):
            add_to_dic(dic["userID"], id)
            print_user_group(id)
            # dict["userID"].append(id)
    print dic

# Function 2, Slice 3:

for i in range(len(nameList)):
    name = nameList[i]
    if (len(name) <= 8 and name == name.lower()):
        # dict["userName"].append(name)
        add_to_dic(dic["userName"], name)

def printArray(array):
    print array