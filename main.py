from random import choice
import csv

with open('flashcards.csv') as cards_file:
    cards = [t for t in csv.reader(cards_file) if t[0] != 'Question']

    while True:
        card = choice(cards)
        print(card[0], end="")
        confirm = input()
        print(card[1], end="\n\n")
