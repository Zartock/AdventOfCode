from ACutils.utils import read_input_to_list_of_strings



def main():
    input_list = read_input_to_list_of_strings("input.txt")

    times = [int(x) for x in input_list[0].split() if x.isdigit()]
    distances = [int(x) for x in input_list[1].split() if x.isdigit()]

    milliseconds = int("".join([str(x) for x in times]))
    goal_distance = int("".join([str(x) for x in distances]))
    ways = 0
    for holding in range(milliseconds + 1):
        if holding * (milliseconds - holding) > goal_distance:
            ways += 1

    print(ways)

main()