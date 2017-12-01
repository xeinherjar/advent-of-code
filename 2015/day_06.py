lights = [False] * 1000 * 1000
lights_day2 = [0] * 1000 * 1000

def run():
    with open('day_06_input', 'r') as f:
        for line in f:
            parsed = line.split(' ')
            if len(parsed) == 4:
                op, start, _, end = parsed
            else:
                op, status, start, _, end = parsed

            start = [int(s) for s in start.split(',')]
            end = [int(s) for s in end.split(',')]

            if op == 'toggle':
                toggle(start, end)
            else:
                if status == 'on':
                    on(start, end)
                else:
                    off(start, end)
    total()


def toggle(start, end):
    number_of_rows = end[0] - start[0] + 1
    number_of_columns = end[1] - start[1] + 1

    for row in range(number_of_rows):
        r = (start[0] + row) * 1000
        for col in range(number_of_columns):
            c = start[1] + col
            point = r + c
            lights[point] = not lights[point]
            lights_day2[point] += 2

def on(start, end):
    number_of_rows = end[0] - start[0] + 1
    number_of_columns = end[1] - start[1] + 1

    for row in range(number_of_rows):
        r = (start[0] + row) * 1000
        for col in range(number_of_columns):
            c = start[1] + col
            point = r + c
            lights[point] = True
            lights_day2[point] += 1

def off(start, end):
    number_of_rows = end[0] - start[0] + 1
    number_of_columns = end[1] - start[1] + 1

    for row in range(number_of_rows):
        r = (start[0] + row) * 1000
        for col in range(number_of_columns):
           c = start[1] + col
           point = r + c
           lights[point] = False
           lights_day2[point] -= 1
           if lights_day2[point] <= 0:
               lights_day2[point] = 0

def total():
    count = 0
    for light in lights:
        if light:
            count = count + 1
    print('Total light count', count)

    count_d2 = sum(lights_day2)
    print('Total brighness', count_d2)

if __name__ == '__main__':
    run()
