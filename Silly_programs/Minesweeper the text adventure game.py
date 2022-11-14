from random import randint


def main():
    print("How big would you like your thing?")
    size = int(input(">>>"))
    print("And what percentage of the board should be mines?")
    mines = float(input(">>>"))
    print("Do you want to print the board with numbers or just mines?")
    nums = input(">>>")
    if nums == "numbers" or nums == "Numbers":
        nums = True
    else:
        nums = False
    print("One last thing, Yes or no: do you want me to draw the completed board?")
    draw = input(">>>")
    if draw == "yes" or draw == "Yes":
        draw = True
    else:
        draw = False
    print("Ok sick, gimme a sec")
    print('''
    
    
    ''')
    grid = [0]
    create(size, mines, draw, nums, grid)


def create(size, mines, draw, nums, grid):
    width = int(size)
    length = int(width * .7)
    mines = length * width * mines
    if mines > length * width:
        mines = length * width

    grid = [[0] * width for _ in range(length)]

    i = 0
    while i < mines:
        rand1 = randint(0, length - 1)
        rand2 = randint(0, width - 1)
        if grid[rand1][rand2] == 9:
            print("Processing")
        else:
            grid[rand1][rand2] = 9
            i += 1

    if nums:
        for i in range(length):
            for t in range(width):
                count = 0
                if grid[i][t] != 9:
                    if i != length - 1:
                        if grid[i + 1][t] == 9:
                            count += 1
                    if i != 0:
                        if grid[i - 1][t] == 9:
                            count += 1
                    if t != width - 1:
                        if grid[i][t + 1] == 9:
                            count += 1
                    if t != 0:
                        if grid[i][t - 1] == 9:
                            count += 1
                    if i != length - 1 and t != width - 1:
                        if grid[i + 1][t + 1] == 9:
                            count += 1
                    if i != length - 1 and t != width:
                        if grid[i + 1][t - 1] == 9:
                            count += 1
                    if i != 0 and t != 0:
                        if grid[i - 1][t - 1] == 9:
                            count += 1
                    if i != 0 and t != width - 1:
                        if grid[i - 1][t + 1] == 9:
                            count += 1
                    grid[i][t] = count

    if draw:
        result = ""
        for i in range(length):
            for t in range(width):
                if grid[i][t] == 0:
                    result += "- "
                elif grid[i][t] == 9:
                    result += "x "
                else:
                    result += str(grid[i][t]) + " "
            print(result)
            result = ""


main()
