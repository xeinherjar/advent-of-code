def run():
    total = 0
    ribbon = 0
    with open('day_02_input', 'r') as f:
        for line in f:
            length, width, height = [int(x) for x in line.split('x')]
            a = length * width
            b = width * height
            c = height * length

            # Calculate Paper
            surface_area = 2 * a + 2 * b + 2 * c
            smallest_side = min([a, b, c])
            total = total + surface_area + smallest_side

            # Calculate Ribbon
            f1, f2 = sorted([length, width, height])[:2]
            ribbon_for_box = f1 + f1 + f2 + f2 + (length * width * height)
            ribbon = ribbon + ribbon_for_box

    print('Total Paper', total)
    print('Total Ribbon', ribbon)

if __name__ == '__main__':
    run()
