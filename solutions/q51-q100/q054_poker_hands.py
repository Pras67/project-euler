"""
Question 54: Poker Hands
URL: https://projecteuler.net/problem=54

In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in the same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value cards wins; for example, a pair of eights beats a pair of fives (see Example 1 below). But if two ranks are equal, for example, both players have a pair of queens, then highest card in each hand is compared (see Example 4 below); if the highest cards are equal then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand 1:
Player 1: 5H 5C 6S 7S KD (Pair of Fives)
Player 2: 2C 3S 8S 8D TD (Pair of Eights)
Winner: Player 2

Hand 2:
Player 1: 5D 8C 9S JS AC (Highest card Ace)
Player 2: 2C 5C 7D 8S QH (Highest card Queen)
Winner: Player 1

Hand 3:
Player 1: 2D 9C AS AH AC (Three Aces)
Player 2: 3D 6D 7D TD QD (Flush with Diamonds)
Winner: Player 2

Hand 4:
Player 1: 4D 6S 9H QH QC (Pair of Queens, highest card Nine)
Player 2: 3D 6D 7H QD QS (Pair of Queens, highest card Seven)
Winner: Player 1

Hand 5:
Player 1: 2H 2D 4C 4D 4S (Full House, With Three Fours)
Player 2: 3C 3D 3S 9S 9D (Full House, with Three Threes)
Winner: Player 1

The file data/poker.txt contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five cards are Player 1's hand and the last five cards are Player 2's hand. You can assume that all hands are valid (no duplicate cards), each player's hand is in no specific order, and that each hand clearly defines a winner.

How many hands does Player 1 win?

Measured Runtime: ~0.007800s
"""

import time
from collections import Counter


def eval_hand(hand: list[str]) -> tuple[int, list[int]]:
    values = "23456789TJQKA"
    value = {v: i for i, v in enumerate(values)}

    ranks = [value[card[0]] for card in hand]
    suits = [card[1] for card in hand]

    counts = Counter(ranks)
    groups = sorted(
        ((count, rank) for rank, count in counts.items()),
        reverse=True
    )

    is_flush = len(set(suits)) == 1

    unique = sorted(set(ranks))

    if unique == [0, 1, 2, 3, 12]:
        straight_high = 3
    elif len(unique) == 5 and unique[-1] - unique[0] == 4:
        straight_high = unique[-1]
    else:
        straight_high = None

    is_straight = straight_high is not None

    if is_straight and is_flush:
        if straight_high == 12:
            return (9, [straight_high])
        return (8, [straight_high])

    if groups[0][0] == 4:
        return (7, [groups[0][1], groups[1][1]])

    if groups[0][0] == 3 and groups[1][0] == 2:
        return (6, [groups[0][1], groups[1][1]])

    if is_flush:
        return (5, sorted(ranks, reverse=True))

    if is_straight:
        return (4, [straight_high])

    if groups[0][0] == 3:
        kickers = sorted(
            [rank for rank in ranks if rank != groups[0][1]],
            reverse=True
        )
        return (3, [groups[0][1]] + kickers)

    if groups[0][0] == 2 and groups[1][0] == 2:
        pairs = sorted(
            [groups[0][1], groups[1][1]],
            reverse=True
        )
        kicker = groups[2][1]
        return (2, pairs + [kicker])

    if groups[0][0] == 2:
        pair = groups[0][1]
        kickers = sorted(
            [rank for rank in ranks if rank != pair],
            reverse=True
        )
        return (1, [pair] + kickers)

    return (0, sorted(ranks, reverse=True))


def solve() -> int:
    player1_wins = 0

    with open("data/poker.txt") as f:
        for line in f:
            cards = line.split()

            hand1 = cards[:5]
            hand2 = cards[5:]

            if eval_hand(hand1) > eval_hand(hand2):
                player1_wins += 1

    return player1_wins


if __name__ == "__main__":
    start_time = time.time()
    result = solve()
    elapsed = time.time() - start_time
    print(f"Result: {result}")
    print(f"Elapsed time: {elapsed:.6f} seconds")