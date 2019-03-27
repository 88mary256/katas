def getCount(line):
    if (line == None or len(line) < 1):
        return 0
    return len(''.join(c for c in line.lower() if c in ['a', 'e', 'i', 'o', 'u']))


'''
clever
def getCount(s):
    return sum(c in 'aeiou' for c in s)
'''
