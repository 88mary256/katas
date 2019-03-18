def urlCapture(text):
    urls = []
    numberChars = len(text)
    indexstart = 0
    while numberChars >= indexstart:
        indexstart = text.find('http://', indexstart)
        if indexstart < 0:
            break
        iindexend = text.find(' ', indexstart)
        urls.append(text[indexstart:iindexend])
        indexstart = iindexend
    print (" ".join(str(x) for x in urls))


urlCapture('Hi http://somewhat.com/url http://somewhat.com/world')