from card import *
import random


class deck():

    def __init__(self):
        self.card_pile= self.set_Up_Deck()

    def set_Up_Deck(self):
        card_pile = []
        # Cards will get assigned a unique ID value
        # starting from 0 to 51 (inclusive)
        for num in range(0,52):
            if num <= 3:
                some_card= card(num, '2', 2)
                card_pile.append(some_card)

            elif num > 3 and num <= 7:
                some_card= card(num, '3', 3)
                card_pile.append(some_card)

            elif num>7 and num <=11:
                some_card=card(num, '4', 4)
                card_pile.append(some_card)

            elif num>11 and num<=15:
                some_card=card(num, '5', 5)
                card_pile.append(some_card)

            elif num > 15 and num <= 19:
                some_card = card(num, '6', 6)
                card_pile.append(some_card)

            elif num > 19 and num <= 23:
                some_card = card(num, '7', 7)
                card_pile.append(some_card)

            elif num > 23 and num <= 27:
                some_card = card(num, '8', 8)
                card_pile.append(some_card)

            elif num > 27 and num <= 31:
                some_card = card(num, '9', 9)
                card_pile.append(some_card)

            elif num > 31 and num <= 35:
                some_card = card(num, '10', 10)
                card_pile.append(some_card)

            elif num > 35 and num <= 39:
                some_card = card(num, 'Jack', 10)
                card_pile.append(some_card)

            elif num > 39 and num <= 43:
                some_card = card(num, 'Queen', 10)
                card_pile.append(some_card)

            elif num > 43 and num <= 47:
                some_card = card(num, 'King', 10)
                card_pile.append(some_card)

            # The scenario that Aces have a value of 1
            # must be handled outside of this class.
            elif num > 47 and num <= 51:
                some_card = card(num, 'Ace', 11)
                card_pile.append(some_card)

        return card_pile

    def shuffle(self):
        # The following will randomly shuffle the indices of the card_pile
        # one hundred times
        for integer in range(0,101):
            # Generates a random number representing one of the indicies within
            # the card_pile
            index1 = random.randint(0,len(self.card_pile)-1)
            index2 = random.randint(0,len(self.card_pile)-1)

            # This will grab the corresponding values at the randomly
            # generated index values from above.
            value1 = self.card_pile.__getitem__(index1)
            value2 = self.card_pile.__getitem__(index2)

            # Swaps the values between the indices to shuffle them.
            self.card_pile[index1] = value2
            self.card_pile[index2] = value1

    def __str__(self):
        card_string=''
        for index, card in enumerate(self.card_pile):
            if index % 4 == 0 and index != 0: #each row has 4 cards
                card_string = card_string + '\n'
            card_string = card_string + card.__str__() + ', '

        return 'Deck: \n' + card_string

    def get_card(self):
        top_card=self.card_pile.pop()
        return top_card

    def is_deck_near_empty(self):
        if len(self.card_pile) <6:
            return True
        else:
            return False


