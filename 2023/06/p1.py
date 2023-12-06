from ACutils.utils import read_input_to_list_of_strings


def main():
    input_list = read_input_to_list_of_strings("input.txt")

    times = [int(x) for x in input_list[0].split() if x.isdigit()]
    distances = [int(x) for x in input_list[1].split() if x.isdigit()]
    number_of_ways = []

    for i, milliseconds in enumerate(times):
        goal_distance = distances[i]
        ways = 0
        for holding in range(milliseconds + 1):
            if holding * (milliseconds - holding) > goal_distance:
                ways += 1
        number_of_ways.append(ways)

    result = 1
    for x in number_of_ways:
        result *= x
    print(result)

main()