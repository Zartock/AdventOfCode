from ACutils.utils import read_input_to_list_of_strings
from typing import List
import collections


def get_formatted_input(input: List[str]):
    result = []
    for row in input:
        tmp = row.split(" ")
        result.append((tmp[0], tmp[1]))
    return result

def sort_cards(cards: str) -> str:
    card_order = "AKQJT98765432"
    return "".join(sorted(cards, key=lambda card: card_order.index(card), reverse=True))


def sort_tuples(lst):
    def key_func(tup):
        # Convert the string to a list of integers
        char_to_int = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'J': 1}
        chars = [char_to_int[char] for char in tup[0]]
        return tup[2], chars

    return sorted(lst, key=key_func)

def get_max_hand(hand: str) -> int:
    ts = []
    for r in 'J23456789TQKA':
        tmp = hand.replace('J', r)
        ts.append(determine_poker_hand(tmp))
    return (max(ts))


def determine_poker_hand(hand: str) -> str:
    card_value = dict(zip('A K Q J T 9 8 7 6 5 4 3 2'.split(), range(13, -1, -1)))
    cards = [card_value[c] for c in hand]
    cards.sort()
    same_cards = sorted([cards.count(c) for c in set(cards)], reverse=True)
    if same_cards == [5]:
        return 7
    elif same_cards == [4, 1]:
        return 6
    elif same_cards == [3, 2]:
        return 5
    elif same_cards == [3, 1, 1]:
        return 4
    elif same_cards == [2, 2, 1]:
        return 3
    elif same_cards == [2, 1, 1, 1]:
        return 2
    else:
        return 1

def main():
    input = read_input_to_list_of_strings("input.txt")
    formatted_input = get_formatted_input(input)
    print(formatted_input)
    first_eval = []
    for x in formatted_input:
        max_hand = get_max_hand(x[0])
        first_eval.append((x[0], x[1], max_hand))
    sorted_list = sort_tuples(first_eval)
    print(sorted_list)
    
    total = 0
    for i in range(0, len(sorted_list)):
        total += int(sorted_list[i][1]) * (i+1)
    print(total)


main()
