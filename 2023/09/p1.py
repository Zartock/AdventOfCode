from ACutils.utils import read_input_to_list_of_strings


def get_diff(line):
    if sum(i != 0 for i in line) == 0:
        return 0
    m = []
    for i in range(len(line) - 1):
        m.append(line[i + 1] - line[i])
    return line[-1] + get_diff(m)


def main():
    input = read_input_to_list_of_strings("input.txt")
    formatted_input = [[int(i) for i in s.split()] for s in input if s.strip()]
    
    result = sum(get_diff(x) for x in formatted_input)
    print("Result: ", result)

main()
