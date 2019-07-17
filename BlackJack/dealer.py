from player import *


class dealer(player):

    def __init__(self, card_deck_to_deal, name = 'Dealer'):
        player.__init__(self,name)
        self.card_deck_to_deal = card_deck_to_deal


    def deal_cards(self,num_cards_to_deal=4):
        dealt_cards = []
        # this will deal a number of cards from the card deck
        # and put it into the dealed_cards list
        for num in range(0, num_cards_to_deal):
            dealt_cards.append(self.card_deck_to_deal.get_card())

        # The following converts the list of dealed cards to a tuple
        # to ensure that it is not further modified outside the method
        dealt_cards_tuple = tuple(dealt_cards)
        return dealt_cards_tuple


    def try_to_beat_player_opponent(self, opponents_cards_value):
        # The following will calculate the total value of the dealer's cards
        # which WILL include the value of their second card which was initially
        # face-down.
        dealers_combined_card_value = self.get_cards_total_value(True)

        # The following will continue to execute UNTIL the dealer's combined-card-
        # value is greater than the opponents OR is greater than 21. Therefore, if the
        # dealer beats the opponent's card value OR the dealer busts OR the dealer gets blackjack,
        # this loop will terminate
        while (dealers_combined_card_value < opponents_cards_value and dealers_combined_card_value < 21) or \
                (dealers_combined_card_value == opponents_cards_value and dealers_combined_card_value < 17):

            # The dealer will pull a card from the deck, put it in
            # their own card pile and recalculate the total combined
            # value of the cards.
            dealt_card = self.deal_cards(1)
            self.received_cards.append(dealt_card[0])
            dealers_combined_card_value = self.get_cards_total_value(True)

        # This statement handles the scenario that the dealer matches the opponent's card value when its
        # greater than or equal to 17. When this occurs, the dealer will not pull anymore cards from the deck
        # and will simply push them.
        if dealers_combined_card_value == opponents_cards_value and dealers_combined_card_value >= 17:
            return 'The dealer matched your card value at {}. Push.'.format(str(opponents_cards_value))

        if dealers_combined_card_value == 21 and opponents_cards_value == 21:
            return 'You and the Dealer both got Blackjack: Push. '

        if dealers_combined_card_value > 21:
            return 'The Dealer busted. You win!'

        if dealers_combined_card_value > opponents_cards_value:
            return 'The Dealer beat you. You lose'

        else: #this should never be reached
            return ''


