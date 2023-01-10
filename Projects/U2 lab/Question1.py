def avg(param1, param2):
    try:
        return (param1 + param2) / 2
    except TypeError:
        return "Please use two numbers as parameters"
