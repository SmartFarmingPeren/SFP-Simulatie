import datetime


def main():
    output_file = "C:/Users/lucav/Documents/GitHub/SFP-Simulatie/SpaceColonizationSim3D/xyz/moooi/test.xyz"
    input_file = "C:/Users/lucav/Documents/GitHub/SFP-Simulatie/SpaceColonizationSim3D/xyz/moooi/gen34_10_03_centroid_thickness.xyz"

    f = open(input_file, "r")
    # print(f.readlines())
    buffer = []
    for line in f.readlines():
        buffer.append(line.split(" "))
    # print(buffer)
    x = 0
    y = 0
    z = 0

    coordinates = []
    for coordinate in buffer:
        x = float(coordinate[0])
        y = float(coordinate[1])
        z = coordinate[2].rstrip("\n")
        z = float(z)

        if x != 0:
            x /= 100
        else:
            x = 0

        if y != 0:
            y /= 100
        else:
            y = 0

        if z != 0:
            z /= 100
        else:
            z = 0

        coordinates.append([x, y, z])

    with open(output_file, 'w') as f:
        for coordinate in coordinates:
            points = str(coordinate[0]) + ' ' + str(coordinate[1]) + ' ' + str(coordinate[2]) + '\n'
            f.write(points)
        f.close()

if __name__ == '__main__':
    main()
