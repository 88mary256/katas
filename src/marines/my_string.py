

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
