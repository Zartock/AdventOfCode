from ACutils.utils import read_input_to_list_of_strings, extract_digits_from_string


def get_formated_input(input):
    result = {}
    for x in input:
        game_nr = int(extract_digits_from_string(x.split(':')[0].strip()))
        result[game_nr] = 1
    return result

def get_score_for_game(row):
    cards = row.split(':')[1].strip()
    winning_cards = cards.split('|')[0].strip().split(" ")
    cards_you_have = cards.split('|')[1].strip().split(" ")
    while '' in winning_cards: winning_cards.remove('') 
    while '' in cards_you_have: cards_you_have.remove('') 

    c = sum(el in winning_cards for el in cards_you_have)
    return c

def main():
    input = read_input_to_list_of_strings("input.txt")
    formatted_input = get_formated_input(input)
    print(formatted_input)
    for key, value in formatted_input.items():
        matches = get_score_for_game(input[key-1])
        if matches == 0:
            continue

        for x in range(1, matches + 1):
            formatted_input[key + x] += value

    print("Result: {}".format(sum(formatted_input.values())))
main()