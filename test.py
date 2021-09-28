def print_2d(grid):
    for array in grid:
        print(array)


def move(grid):
    modified = []
    for array in grid:
        for i in range(1, len(array)):
            if array[i] == 0:
                continue
            for j in range(i - 1, -1, -1):
                if array[j] == 0 and not j == 0:
                    continue
                elif array[j] == 0 and j == 0:
                    array[j] = array[i]
                    array[i] = 0
                    break
                elif not array[j] == array[i] and j + 1 == i:
                    break
                elif array[j] == array[i]:
                    array[j] *= 2
                    array[i] = 0
                    break
                elif not array[j] == array[i] and not j + 1 == i:
                    array[j + 1] = array[i]
                    array[i] = 0
                    break
        modified.append(array)

    return modified


grid = [[0, 1, 2, 3],
        [4, 0, 0, 0],
        [8, 0, 2, 0],
        [12, 0, 0, 0]]

print_2d(grid)
print(" ")
print_2d(move(grid))
