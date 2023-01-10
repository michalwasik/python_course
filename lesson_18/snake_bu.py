from random import randint
from time import sleep
# snake
area = [[]for _ in range(20)]
for _ in range(40): area[0].append('+')
for x in range(1, 19):
    area[x].append('+')
    for _ in range(38): area[x].append(' ')
    area[x].append('+')
for _ in range(40): area[-1].append('+')


def show_game():
    for i in area:
        a = ''.join(i)
        print(a)


def crash(coord):
    if area[coord[0]][coord[1]] in ['0', '+']:
        raise Exception(f"Sorry, you lost '\n' Your score:{len(snake)}")


snake = [(10, 10), (11, 10)]
head_direction = [1, 0]
fruit = []
trace = []


def show_head(direction):
    if direction == [1, 0]:
        return '^'
    elif direction == [-1, 0]:
        return 'v'
    elif direction == [0, -1]:
        return '>'
    else:
        return '<'


def show_snake(show=True):
    for idx, (x, y) in enumerate(snake):
        if idx == 0:
            head = show_head(get_head_dir(snake))
            area[x][y] = head
        else:
            area[x][y] = '0'
    if show:
        show_game()
        sleep(0.001)


def get_head_dir(snake):
    head_dir = [
        snake[1][0] - snake[0][0],
        snake[1][1] - snake[0][1]
    ]
    return head_dir


while True:
    if not fruit:
        while True:
            fruit = [randint(1, 19), randint(1, 39)]
            if area[fruit[0]][fruit[1]] == ' ':
                area[fruit[0]][fruit[1]] = '*'
                show_snake(show=False)
                break
    else:
        if list(snake[0]) == fruit:
            snake.append(tuple(trace))
            show_snake()
            trace = []
            fruit = []
        else:
            way = [snake[0][0] - fruit[0], snake[0][1] - fruit[1]]
            head_direction = get_head_dir(snake)
            if way[0] * head_direction[0] < 0:
                if area[snake[0][0]][snake[0][1] - 1] not in ['+', '0']:
                    trace = snake[-1]
                    area[trace[0]][trace[1]] = ' '
                    snake.insert(0, (snake[0][0], snake[0][1] - 1))
                    snake = snake[:-1]
                    crash(snake[0])
                else:
                    trace = snake[-1]
                    area[trace[0]][trace[1]] = ' '
                    snake.insert(0, (snake[0][0], snake[0][1] + 1))
                    snake = snake[:-1]
                    crash(snake[0])
                way = [snake[0][0] - fruit[0], snake[0][1] - fruit[1]]
            elif way[0] == 0:
                if area[snake[0][0] - 1][snake[0][1]] not in ['+', '0']:
                    trace = snake[-1]
                    area[trace[0]][trace[1]] = ' '
                    snake.insert(0, (snake[0][0] - 1, snake[0][1]))
                    snake = snake[:-1]
                    show_snake()
                    crash(snake[0])
                else:
                    trace = snake[-1]
                    area[trace[0]][trace[1]] = ' '
                    snake.insert(0, (snake[0][0] + 1, snake[0][1]))
                    snake = snake[:-1]
                    show_snake()
                    crash(snake[0])
                way = [snake[0][0] - fruit[0], snake[0][1] - fruit[1]]
            while way[0] != 0:
                if snake[0][0] - fruit[0] > 0:
                    move = -1
                else:
                    move = 1
                if area[snake[0][0] + move][snake[0][1]] in ['+', '0']:
                    if area[snake[0][0]][snake[0][1] - 1] not in ['+', '0']:
                        trace = snake[-1]
                        area[trace[0]][trace[1]] = ' '
                        snake.insert(0, (snake[0][0], snake[0][1] - 1))
                        snake = snake[:-1]
                        show_snake()
                        crash(snake[0])
                    else:
                        trace = snake[-1]
                        area[trace[0]][trace[1]] = ' '
                        snake.insert(0, (snake[0][0], snake[0][1] + 1))
                        snake = snake[:-1]
                        crash(snake[0])
                        show_snake()
                    way = [snake[0][0] - fruit[0], snake[0][1] - fruit[1]]
                else:
                    trace = list(snake[-1])
                    area[trace[0]][trace[1]] = ' '
                    snake.insert(0, (snake[0][0] + move, snake[0][1]))
                    snake = snake[:-1]
                    crash(snake[0])
                    way = [snake[0][0] - fruit[0], snake[0][1] - fruit[1]]
                    show_snake()
            while way[1] != 0:
                if snake[0][1] - fruit[1] > 0:
                    move = -1
                else:
                    move = 1
                if area[snake[0][0]][snake[0][1] + move] in ['+', '0']:
                    if area[snake[0][0] - 1][snake[0][1]] not in ['+', '0']:
                        trace = snake[-1]
                        area[trace[0]][trace[1]] = ' '
                        snake.insert(0, (snake[0][0] - 1, snake[0][1]))
                        snake = snake[:-1]
                        crash(snake[0])
                        show_snake()
                    else:
                        trace = snake[-1]
                        area[trace[0]][trace[1]] = ' '
                        snake.insert(0, (snake[0][0] + 1, snake[0][1]))
                        snake = snake[:-1]
                        crash(snake[0])
                        show_snake()
                    way = [snake[0][0] - fruit[0], snake[0][1] - fruit[1]]
                else:
                    trace = list(snake[-1])
                    area[trace[0]][trace[1]] = ' '
                    snake.insert(0, (snake[0][0], snake[0][1] + move))
                    snake = snake[:-1]
                    crash(snake[0])
                    way = [snake[0][0] - fruit[0], snake[0][1] - fruit[1]]
                    show_snake()

