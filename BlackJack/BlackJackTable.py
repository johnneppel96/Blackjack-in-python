from deck import *
from dealer import *
from player import *
import sys
import time
import os
from colorama import *

colorama = ''


def intro_prompt():
    while True:
        selection = input('Welcome to Blackjack! \nEnter 1 to get stated. \nEnter 2 to quit\n')
        if selection == '1':
            break

        elif selection == '2':
            print('Until next time, bro')
            sys.exit()

        else:
            print('Wut??')


def print_cards(cards=(),  incl_last_card=True):

    for index, a_card in enumerate(cards):
        name = a_card.get_name()

        # 'face_value' will represent the character that appears
        # on the front of the card e.g: K, J, Q 2
        if name == 'Jack' or name == 'Queen' or name == 'King' or name == 'Ace':
            face_value = name[0]  # These cards simply have the first letter representing their face value

        else:
            face_value = str(a_card.get_value())

        # The following will print a blank/face-down card
        # in place of printing the actual contents of the card.
        # This mimics a dealer putting down a card face-down.
        # The following block is only printed if the second parameter
        # in the function is False and its currently the last card in the cards parameter tuple.
        if incl_last_card == False and (index == len(cards)-1):
            print_face_down_card()
            break

        # Since the face value of the card '10'
        # is two characters long, it has a tendency
        # to mess up the particular print-formatting of
        # the card. Therefore, the formatting of the print
        # is reduced by one space to allow for accurate printing
        # of the additional character.
        if face_value == '10':
            print('_______\n'
                  f'|   {face_value}' '|\n'
                  '|     |\n'
                  '|' f' {face_value}'  '  |\n'
                  '|_____|\n'
                  'Card: ' + a_card.get_name() + '\n', end="")

        else:
         print('_______\n'
                f'|   {face_value}' ' |\n'
                 '|     |\n'
                '|' f' {face_value}'  '   |\n'
                '|_____|\n'
                'Card: ' + a_card.get_name() +'\n', end = "")





def print_face_down_card():
   print( '________\n'
    '|******|\n'
    '|******|\n'
    '|******|\n'
    '|______|\n' )


def get_hit_or_stand_input():
    user_input = input('Do you want to Hit or Stand? \n')
    while True:
        if user_input.lower() == 'hit':
            print()
            return 'hit'

        if user_input.lower() == 'stand':
            print()
            return 'stand'

        else:
             user_input = input("I'm not sure what you inputted, please enter hit or stand to continue \n")


def print_separation_line():
    print(Fore.YELLOW + '###########################' + Style.RESET_ALL)


def clear_screen():
    os.system('cls')


def determine_dealt_cards_result(cards_combined_value):
    if cards_combined_value < 21:
        return 'UNDER 21'

    if cards_combined_value == 21:
        return 'BLACKJACK'

    else:
        return 'BUST'


def should_we_keep_playing():
    response = input('Want to keep playing? Enter Yes or No. \n')
    clear_screen()
    print_separation_line()
    if response.lower() == 'yes':
        return True
    else:
        return False


def print_player_cards_info(blackjack_player):
    print(Fore.CYAN + '{} cards: '.format(blackjack_player.get_name()))
    print_cards(Player1.get_dealt_cards(), True)
    print(Fore.CYAN + '{} combined card value: {} '.format(blackjack_player.get_name(), Player1.get_cards_total_value(True)))
    print_separation_line()


def print_dealer_cards_info(blackjack_dealer, inc_last_card = True):
    print(Fore.MAGENTA + "{}'s cards: ".format(blackjack_dealer.get_name()))
    print_cards(Dealer.get_dealt_cards(), inc_last_card)
    print(Fore.MAGENTA + '{} combined card value: {}'.format(blackjack_dealer.get_name(), Dealer.get_cards_total_value(inc_last_card)))
    print_separation_line()


if __name__ == '__main__':
    colorama.__init__(autoreset= True)
    a_deck_of_cards = deck()
    a_deck_of_cards.shuffle()
    Player1 = player('Your')
    Dealer = dealer(a_deck_of_cards, 'Dealer')

    intro_prompt()

    while a_deck_of_cards.is_deck_near_empty() == False:
        picked_cards = Dealer.deal_cards(4)

        # Pulls cards from the dealt cards above and
        # assigns them to the appropriate player/dealer variables
        Player1.give_dealt_card(picked_cards[0])
        Dealer.give_dealt_card(picked_cards[1])
        Player1.give_dealt_card(picked_cards[2])
        Dealer.give_dealt_card(picked_cards[3])

        # This will print the dealer's cards to the screen (one will be face-down),
        # calculate the value of the face-up card and output that value to the screen as well.
        print_dealer_cards_info(Dealer, False)

        # This will print the player's cards to the screen (both will be face up),
        # calculate the total value of all the cards and determine the result of
        # the set of cards (e.g whether it's blackjack or a value under 21)
        print_player_cards_info(Player1)

        # Determines whether the player got blackjack or simply got a combined card value
        # less than 21
        result_of_players_cards = determine_dealt_cards_result(Player1.get_cards_total_value())

        # First checks to see if player got blackjack with their two dealt cards
        if result_of_players_cards == 'BLACKJACK':
            print('YOU GOT BLACKJACK!\n***********************')
            time.sleep(2)

            # The dealer here will attempt to match the player's
            # blackjack by revealing the value of their second/face-down
            # card and pulling more cards from the deck if necessary. The
            # dealer will either match/push against the opposing player or
            # bust.
            result_of_dealers_cards = Dealer.try_to_beat_player_opponent(Player1.get_cards_total_value())
            print_dealer_cards_info(Dealer, True)
            print(result_of_dealers_cards)

            if result_of_dealers_cards == 'You and the Dealer both got Blackjack: Push ':
                pass

            elif 'The Dealer busted. You win!':
                pass

        # If the player didn't get blackjack with their two dealt cards,
        # the only other possible scenario is that they got a total score less than
        # 21 and hence will enter the following code block
        else:
            players_decision = get_hit_or_stand_input()
            clear_screen()
            print_separation_line()

            while players_decision == 'hit':
                picked_cards = Dealer.deal_cards(1)
                Player1.give_dealt_card(picked_cards[0])
                print_player_cards_info(Player1)
                result_of_players_cards =  determine_dealt_cards_result(Player1.get_cards_total_value(True))
                clear_screen()

                if result_of_players_cards == 'BUST':
                    print_dealer_cards_info(Dealer, True)
                    print_player_cards_info(Player1)
                    print('You busted. You lose')
                    # in the case of a BUST, the player's decision is automatically
                    # altered to 'Done' to ensure it doesn't enter anymore blocks of code
                    # below and to ensure that encompassing 'while' loop above is no longer executed
                    players_decision = 'Done'

                if result_of_players_cards == 'BLACKJACK':
                    print_player_cards_info(Player1)
                    print('YOU GOT BLACKJACK!\n***********************')
                    time.sleep(2)
                    players_decision = 'stand'

                if result_of_players_cards == 'UNDER 21':
                    print_dealer_cards_info(Dealer, False)
                    print_player_cards_info(Player1)
                    players_decision = get_hit_or_stand_input()
                    clear_screen()
                    print_separation_line()

            if players_decision == 'stand':  # If the player chooses to stand
                result_of_dealers_cards = Dealer.try_to_beat_player_opponent(Player1.get_cards_total_value())
                print_dealer_cards_info(Dealer, True)
                print_player_cards_info(Player1)
                print(result_of_dealers_cards)

        if should_we_keep_playing():
            Dealer.take_away_cards()
            Player1.take_away_cards()
            continue

        else:
            sys.exit(11)








