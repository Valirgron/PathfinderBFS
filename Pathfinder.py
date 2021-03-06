import queue
import sys


def createMaze():
    maze = []
    maze.append(["#","O", "#", "#", "#"])
    maze.append([" "," ", "#", "#", " "])
    maze.append(["#","#", " ", "#", " "])
    maze.append([" ","#", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#"])
    maze.append([" ","#", " ", "#", "#"])
    maze.append(["#","#", "X", "#", "#"])

    return maze


def printMaze(maze, path=""):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    pos = set()
    for move in path:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        elif move == "A":
            i -= 1
            j -= 1

        elif move == "B":
            i += 1
            j -= 1

        elif move == "M":
            i -= 1
            j += 1

        elif move == "N":
            i += 1
            j += 1
        pos.add((j, i))

    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in pos:
                sys.stdout.write("+ ")
            else:
                sys.stdout.write(col + " ")
        sys.stdout.write('\n')


def valid(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        elif move == "A":
            i -= 1
            j -= 1

        elif move == "B":
            i += 1
            j -= 1

        elif move == "M":
            i -= 1
            j += 1

        elif move == "N":
            i += 1
            j += 1

        if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "#"):
            return False

    return True


def findEnd(maze, moves):

    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        elif move == "A":
            i -= 1
            j -= 1

        elif move == "B":
            i += 1
            j -= 1

        elif move == "M":
            i -= 1
            j += 1

        elif move == "N":
            i += 1
            j += 1

    if maze[j][i] == "X":
        print("Found: " + moves)
        printMaze(maze, moves)
        return True

    return False


# MAIN ALGORITHM

nums = queue.Queue()
nums.put("")
add = ""
maze = createMaze()
x = 0
while not findEnd(maze, add):
    x += 1

    print(add)
    add = nums.get()
    print("Tatoshka", add)
    for j in ["L", "R", "U", "D", "A", "B", "M", "N"]:
        x += 1
        put = add + j

        if valid(maze, put):
            print(x)
            nums.put(put)
        