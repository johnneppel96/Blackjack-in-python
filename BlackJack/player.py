class player():

    def __init__(self, name=' '):
        self.name = name
        self.received_cards = []

    def give_dealt_card(self, a_card):
        self.received_cards.append(a_card)

    def take_away_cards(self):
        self.received_cards.clear()

    def get_name(self):
        return self.name

    def get_dealt_cards(self):
        return self.received_cards

    def get_cards_total_value(self, incl_last_cards_value=True):
        total_card_value = 0
        num_of_aces = 0
        for index, a_card in enumerate(self.received_cards):

            # The second/boolean parameter represents whether the last
            # card in the cards deck should be included within the total
            # value of the dealt card deck. This is to ensure that total value
            # of the dealer's cards isn't revealed when necessary (e.g when the
            # cards are initially dealt)
            if incl_last_cards_value == False and index == (len(self.received_cards) - 1):
                break
            else:
                if a_card.get_name() == 'Ace':
                    num_of_aces = num_of_aces + 1

                total_card_value = total_card_value + a_card.get_value()

        # This loop will make the value of their dealt aces equal to 1
        # if the player's total value is a busted value over 21
        while total_card_value > 21 and num_of_aces > 0:
            total_card_value = total_card_value - 10
            num_of_aces = num_of_aces - 1

        return total_card_value





