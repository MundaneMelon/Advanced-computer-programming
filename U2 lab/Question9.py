def reverse_string(string):
    if len(string) == 0:
        return ""
    return string[-1] + reverse_string(string[0:-1])
