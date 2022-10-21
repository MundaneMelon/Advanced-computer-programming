def avg(param1, param2):
    try:
        return (int(param1) + int(param2)) / 2
    except ValueError:
        return "Please use two numbers as parameters"