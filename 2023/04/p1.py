from ACutils.utils import read_input_to_list_of_strings


def main():
    input = read_input_to_list_of_strings("input.txt")
    total = 0
    for line in input:
        cards = line.split(':')[1].strip()
        winning_cards = cards.split('|')[0].strip().split(" ")
        cards_you_have = cards.split('|')[1].strip().split(" ")
        while '' in winning_cards: winning_cards.remove('') 
        while '' in cards_you_have: cards_you_have.remove('') 

        c = sum(el in winning_cards for el in cards_you_have)

        if c == 0:
            continue
        total += pow(2, c-1)
    
    print("Result: {}".format(total))

main()
