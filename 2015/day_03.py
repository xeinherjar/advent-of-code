def run():
    houses = set()
    santa_and_robot_houses = set()

    # They start at house 0,0
    houses.add( (0,0) )
    santa_and_robot_houses.add( (0,0) )
    santa = True
    with open('day_03_input', 'r') as f:
        santa_house = [0, 0]
        robot_house = [0, 0]
        house = [0, 0]
        for line in f:
            for idx, arrow in enumerate(line):
                if (arrow.isspace()):
                    continue

                sr_house = santa_house if santa else robot_house
                santa = not santa

                if arrow == '>':
                    house[0] += 1
                    sr_house[0] += 1
                elif arrow == '<':
                    house[0] -= 1
                    sr_house[0] -= 1
                elif arrow == '^':
                    house[1] += 1
                    sr_house[1] += 1
                elif arrow == 'v':
                    house[1] -= 1
                    sr_house[1] -= 1

                house_xy = (house[0], house[1])
                sr_house_xy = (sr_house[0], sr_house[1])
                houses.add(house_xy)
                santa_and_robot_houses.add(sr_house_xy)

    print('Visted Houses:', len(houses))
    print('Santa and Robot visted houses', len(santa_and_robot_houses))

if __name__ == '__main__':
    run()
