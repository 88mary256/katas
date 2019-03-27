dic = {"userID": {}, "userName": {}}


def get_first(string):
    s = str(string)
    return s[0] if (len(s) > 0) else ""


def add_to_dic(dicfield, value):
    id = get_first(value)
    if (id not in dicfield):
        dicfield[id] = [value]
    else:
        dicfield[id].append(value)


def load_dictionary(idList, nameList):
    print idList
    print nameList

    for i in range(len(idList)):
        id = int(idList[i])
        if (1 <= id <= 100):
            add_to_dic(dic["userID"], id)
            print_user_group(id)
            # dict["userID"].append(id)
    print dic
    for i in range(len(nameList)):
        name = nameList[i]
        if (len(name) <= 8 and name == name.lower()):
            # dict["userName"].append(name)
            add_to_dic(dic["userName"], name)


def find_users_by_first_id_digit(digit):
    if (digit > 9):
        print "please only use 1 digit"
        return []
    return dic["userID"][str(digit)]


def find_users_by_first_char_name(ch):
    if (len(ch) > 1):
        print "please only use 1 character"
        return []
    return dic["userName"][str(ch)]


def printArray(array):
    print array


def print_user_group(id):
    if (1 <= id <= 25):
        print "User belong Group 1"
    if (26 <= id <= 50):
        print "User belong Group 2"
    if (51 <= id <= 75):
        print "User belong Group 3"
    if (76 <= id <= 100):
        print "User belong Group 4"


def execute():
    ids = raw_input("please provide user ids")
    names = raw_input("please provide user names")
    load_dictionary(ids.split(","), names.split(","))
    print dic
    find_users_by_first_id_digit(1)
    find_users_by_first_char_name('m')

def isNewDic():
    return len(dic["userID"]) < 1

