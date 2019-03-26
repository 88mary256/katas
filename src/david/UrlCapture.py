class Url:

    @staticmethod
    def urlcapture(text):
        urls = []
        n = len(text)
        indexstart = 0
        while n >= indexstart:
            indexstart = text.find('http://', indexstart)
            if indexstart < 0:
                break
            iindexend = text.find(' ', indexstart)
            urls.append(text[indexstart:iindexend])
            indexstart = iindexend
        return " ".join(str(x) for x in urls)

