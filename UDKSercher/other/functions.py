
def is_udk_index(string: str):
    repl_string = string.replace(".", "").replace("/", "").replace("-", "")
    if repl_string.isdigit():
        return True
    else:
        return False


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
                    return string[i + 1:]
                else:
                    return string[i:]
    return string


def main():
    udk = "23597/.508"
    print(is_udk_index(udk))


if __name__ == "__main__":
    main()