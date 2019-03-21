def reverse_alternate(string):
    s = string.split(" ")
    result = ""
    for i, single in enumerate(s):
        rs = single[::-1] if i % 2 != 0 else single
        result = result + rs.strip() + " "
    return result.strip()


print reverse_alternate("I really hope it works this time...")