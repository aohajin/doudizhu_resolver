"""
斗地主明牌残局解答器
~~~~~~~~~~
usage:
    >>> import doudizhu_resolver
    >>> doudizhu_resolver.find_strategy('As-Ac-9c','2h-Qd-Qh-10d-10h-7d-7h-5d-5h','3d')
all winable strategies:
pass
    >>> doudizhu_resolver.find_strategy('As-Ac-9c','2h-Qd-Qh-10d-10h-7d-7h-5d','3h')
all winable strategies:
  [ 9 ♣ ]
    >>> doudizhu_resolver.find_strategy('2h-Qd-Qh-10d-10h-7d-7h-5d-5h-3h', 'As-9s')
all winable strategies:
  [ 3 ❤ ]
  [ 10 ❤ ]
  [ Q ❤ ]
  [ 2 ❤ ]
  [ 5 ❤ ], [ 5 ♦ ]
  [ 7 ❤ ], [ 7 ♦ ]
  [ 10 ♦ ], [ 10 ❤ ]
  [ Q ♦ ], [ Q ❤ ]
    >>> doudizhu_resolver.find_strategy('2h-Qd-Qh-10d-10h-7d-7h-5d-5h-3h','As-Ac-9c')
you have already lost.
"""

from doudizhu_resolver import play


def clear_cache():
    play.PLAY_CACHE = {}


def is_winable(my_hand: str, enemy_hand: str) -> bool:
    return play.try_play(0, play.Card.card_ints_from_string(my_hand), play.Card.card_ints_from_string(enemy_hand), [])


def find_strategy(my_hand: str, enemy_hand: str, last_play: str = None):
    play.show_strategy(play.try_win(0, play.Card.card_ints_from_string(
        my_hand), play.Card.card_ints_from_string(enemy_hand), play.Card.card_ints_from_string(last_play) if last_play else []))


__all__ = ['clear_cache', 'is_winable', 'find_strategy']
