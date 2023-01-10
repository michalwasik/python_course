data = open('grid.txt', 'r').read().splitlines()
maze = []
numbers = {}
for idx_x, x in enumerate(data):
    line = []
    for idx_y, y in enumerate(x):
        line.append(y)
        if y.isdecimal():
            numbers[y] = (idx_x, idx_y)
    maze.append(line)

size = (len(maze), len(maze[0]))
start = (1, 1)
stop = (33, 169)


def get_neighbours(point: tuple) -> list[tuple]:
    points = [(point[0]-1, point[1]), (point[0]+1, point[1]),
              (point[0], point[1]-1), (point[0], point[1]+1)]
    valid_points = []
    for candidate in points:
        if candidate[0] in range(size[0]) and candidate[1] in range(size[1]):
            if maze[candidate[0]][candidate[1]] != '#':
                valid_points.append(candidate)
    return valid_points


def recur_func(ways: list[list[tuple]], visited: set, finish: tuple):
    new_ways = []
    for way in ways:
        last_step = way[-1]
        last_step_good = get_neighbours(last_step)
        for new_direction in last_step_good:
            if new_direction not in visited:
                curr_way = way.copy()
                curr_way.append(new_direction)
                new_ways.append(curr_way)
                visited.add(new_direction)
                if new_direction == finish:
                    return len(way)
    if new_ways:
        return recur_func(new_ways, visited, finish)
    else:
        return False


correct_way = (recur_func([[start]], set(start), stop))
# for step in correct_way:
#     maze[step[0]][step[1]] = '■'
# for i in maze:
#     print(i)

bridges = dict()
for num in numbers:
    bridges[num] = dict()
for start_point in numbers:
    start_point = str(start_point)
    for other_point in numbers:
        other_point = str(other_point)
        if other_point != start_point:
            if other_point in bridges:
                if start_point in bridges[other_point]:
                    bridges[start_point][other_point] = bridges[other_point][start_point]
                else:
                    bridges[start_point][other_point] = recur_func([[numbers[start_point]]], set(numbers[start_point]), numbers[other_point])


from itertools import permutations
l = list(permutations(range(1, 8)))
atw = dict()
for perm in l:
    steps = 0
    for no, trip in enumerate(perm):
        if no == 0:
            steps += bridges['0'][str(trip)]
        elif no == 6:
            steps += bridges[str(perm[no - 1])][str(perm[no])]
            steps += bridges[str(trip)]['0']
        else:
            steps += bridges[str(perm[no-1])][str(perm[no])]
    atw[perm] = steps
print(min(atw.values()))

l2 = list(permutations(range(0, 8)))
atw2 = dict()
for perm in l2:
    steps = 0
    for no, trip in enumerate(perm):
        if no < 7:
            steps += bridges[str(perm[no])][str(perm[no+1])]
    atw2[perm] = steps
print(min(atw2.values()))
