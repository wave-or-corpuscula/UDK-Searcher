

string = "www.teacode.com/online/udc/index.html"

def delete_to_first_char(string: str, char: str, del_border: bool = False, from_end: bool = True):
    del_index = -1
    if from_end:
        for i in range(len(string) - 1, 0, -1):
            if (string[i] == char):
                del_index = i
                if del_border:
                    return string[:i]
                else:
                    return string[:(i + 1)]
    else:
        for i in range(len(string)):
            if (string[i] == char):
                del_index = i
                if del_border:
                    return string[:i]
                else:
                    return string[:(i + 1)]
    return string


print(delete_to_first_char(string, "7"))