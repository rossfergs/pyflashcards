from random import choice;import csv;import os
with open('flashcards.csv') as cards_file:
    os.system("clear")
    cards = [t for t in csv.reader(cards_file) if t[0] != 'Question']
    qs = []
    while True:
        card = choice(cards)
        while card[0] in qs:
            card = choice(cards)
        print(card[0], end="")
        confirm = input()
        qs.append(card[0])
        if len(qs) > 5:
            qs.pop(0)
        print(card[1], end="\n")
        confirm = input()
        os.system("clear")

