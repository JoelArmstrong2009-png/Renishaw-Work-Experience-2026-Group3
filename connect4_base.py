def start():
    global grid
    global x_rows
    global y_colums
    x_rows = 9
    y_colums = 6
    grid = []

    for y in range(y_colums):
        grid.append([])
        for x in range(x_rows):
            grid[y].append(" ")

def print_grid():
    for y in range(y_colums):
        for x in range(x_rows):
            print(grid[y][x],end="")
        print()



def drop(x_pos,turn):
    y_drop = 0
    valid = False
    while y_drop != 5 and not valid:
        if grid[y_drop + 1][x_pos] == " ":
            y_drop += 1
        else:
            valid = True
            grid[y_drop][x_pos] = turn
    if not valid:
        grid[y_drop][x_pos] = turn


def main():
    win = False
    turn = "Y"
    while not win:
        if turn == "R":
            turn = "Y"
        elif turn == "Y":
            turn = "R"

        valid = False
        while not valid:
            drop_point = int(input("Drop: "))
            if grid[0][drop_point] == " ":
                valid = True
        drop(drop_point, turn)
        print_grid()

start()
main()