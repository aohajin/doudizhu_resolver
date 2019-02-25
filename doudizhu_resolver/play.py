from .doudizhu import Card, list_greater_cards, list_playable_cards


PLAY_CACHE = {}


def play_card(hand: list, cards: list) -> list:
    dup = hand.copy()
    for card in cards:
        dup.remove(card)
    return dup


def play_log(turn: int, cards: list) -> str:
    name = "me" if turn % 2 == 0 else 'enemy'

    if not cards:
        return '{} -> pass'.format(name)
    return '{} -> {}'.format(name, Card.get_pretty_cards(list(cards)))


def try_play(turn: int, my_hand: list, enemy_hand: list, last_play: list):
    situation = (tuple(Card.sort_cards_by_rank_int(my_hand)), tuple(
        Card.sort_cards_by_rank_int(enemy_hand)), tuple(Card.sort_cards_by_rank_int(last_play)))

    if situation in PLAY_CACHE:
        return PLAY_CACHE[situation]

    if not my_hand:
        return True
    if not enemy_hand:
        return False

    if last_play:
        # 尝试pass
        # new_log = log.copy()
        # new_log.append(play_log(turn, []))

        if not try_play(turn+1, enemy_hand, my_hand, []):
            PLAY_CACHE[situation] = True
            return True

        # 尝试出牌
        playables = list_greater_cards(last_play, my_hand)

        for _, play_list in playables.items():
            for card_list in play_list:

                # new_log = log.copy()
                # new_log.append(play_log(turn, card_list))

                if not try_play(turn+1, enemy_hand, play_card(my_hand, card_list), card_list):
                    PLAY_CACHE[situation] = True
                    return True
    else:
        # 尝试出牌
        playables = list_playable_cards(my_hand)

        # 如果已经可以直接获胜那么就用直接获胜的出法出牌
        for card_list in playables:
            if not play_card(my_hand, card_list):
                # new_log = log.copy()
                # new_log.append(play_log(turn, card_list))

                # for log
                if not try_play(turn+1, enemy_hand, [], card_list):
                    PLAY_CACHE[situation] = True
                    return True

        for card_list in playables:
            # new_log = log.copy()
            # new_log.append(play_log(turn, card_list))

            if not try_play(turn+1, enemy_hand, play_card(my_hand, card_list), card_list):
                PLAY_CACHE[situation] = True
                return True
    # 都没戏，gg
    PLAY_CACHE[situation] = False
    return False


def show_strategy(plays: list):
    if not plays:
        print('you have already lost.')
        return

    print("all winable strategies:")
    for play in plays:
        if play:
            Card.print_pretty_cards(play)
        else:
            print('pass')


def try_win(turn: int, my_hand: list, enemy_hand: list, last_play: list) -> list:
    winable_plays = []
    if last_play:
        # 尝试pass
        # new_log = log.copy()
        # new_log.append(play_log(turn, []))

        if not try_play(turn+1, enemy_hand, my_hand, []):
            winable_plays.append([])
            # return True

        # 尝试出牌
        playables = list_greater_cards(last_play, my_hand)

        for _, play_list in playables.items():
            for card_list in play_list:

                # new_log = log.copy()
                # new_log.append(play_log(turn, card_list))

                if not try_play(turn+1, enemy_hand, play_card(my_hand, card_list), card_list):
                    winable_plays.append(card_list)
                    # return True
    else:
        # 尝试出牌
        playables = list_playable_cards(my_hand)

        # 如果已经可以直接获胜那么就用直接获胜的出法出牌
        for card_list in playables:
            if not play_card(my_hand, card_list):
                # new_log = log.copy()
                # new_log.append(play_log(turn, card_list))
                winable_plays.append(card_list)
                # return True

        for card_list in playables:
            # new_log = log.copy()
            # new_log.append(play_log(turn, card_list))

            if not try_play(turn+1, enemy_hand, play_card(my_hand, card_list), card_list):
                winable_plays.append(card_list)
                # return True

    return winable_plays


# cache = {}
# try_play(0, Card.card_ints_from_string('CJ-BJ-7c-7d-6c-3s-3h'),
#         Card.card_ints_from_string('8s-8h-8d-8c-4d-4h'), [], [])


# if try_play(0, Card.card_ints_from_string('2h-Qd-Qh-10d-10h-7d-7h-5d-5h-3d'),
#            Card.card_ints_from_string('As-Ac-9c'), []):
    # if try_play(0, Card.card_ints_from_string('CJ-BJ-7c-7d-6c-3s-3h'),
    #            Card.card_ints_from_string('8s-8h-8d-8c-4d-4h'), []):
#    print('winable')
# else:
#    print('doomed')

# show_strategy(try_win(1, Card.card_ints_from_string('As-Ac-9c'), Card.card_ints_from_string('2h-Qd-Qh-10d-10h-7d-7h-5d-5h'),
#                      Card.card_ints_from_string('3d')))
