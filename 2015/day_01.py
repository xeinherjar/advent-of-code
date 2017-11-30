def run():
    floor = 0
    basement = 0
    with open('day_01_input', 'r') as f:
        for line in f:
            for idx, ch in enumerate(line):
                if ch == '(':
                    floor = floor + 1
                elif ch == ')':
                    floor = floor - 1

                if floor == -1 and basement == 0:
                    basement = idx + 1

    print('Floor:', floor)
    print('Basement on:', basement)

if __name__ == '__main__':
    run()
