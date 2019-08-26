## SOLVED
## the possible way of solving this is to make a scoring of the hand
## of each player, by encoding the category of winning and the cards
import csv

value = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
val_order = {k:v for v,k in enumerate(value)}

def compute():
    poker_hand = load_data()
    ans = sum(1 for x in poker_hand if p1_wins(x))
    return ans

## is player1 wins?
def p1_wins(hands):
    p1 = [(a[0], a[1]) for a in hands[:5]]  # (value, suit)
    p2 = [(a[0], a[1]) for a in hands[5:]]
    return get_score(p1) > get_score(p2)

## return the score of the hand of a player
## score based on encoded value, using shift bit
def get_score(hand):
    val = [x[0] for x in hand]
    suit = [x[1] for x in hand]

    val_int = [val_order[x] for x in val]
    straight = get_straight(val_int)
    flush = get_flush(suit)

    # list of how many times 'n' occurs
    val_count = [sum(1 for x in val_int if x==i) for i in range(13)]
    # the histogram, how many times a count occurs
    # so if there is one triple, vc_hist[3] = 1
    vc_hist = [0] + [val_count.count(i) for i in range(1, 6)]

    if straight == 12:                  # royal flush
        return (9 << 10)
    elif straight >= 0 and flush == 1:   # straight flush
        return (8 << 10) + straight
    elif vc_hist[4] == 1:               # four of a kind
        return (7 << 10) + (val_count.index(4) << 2) + val_count.index(1)
    elif vc_hist[3] == 1 and vc_hist[2] == 1: # full house
        return (6 << 10) + (val_count.index(3) << 2) + val_count.index(2)
    elif flush == 1:                    # flush
        return (5 << 10) + get_best_high(val_int)
    elif straight >= 0:                  # straight
        return (4 << 10) + straight
    elif vc_hist[3] == 1:               # three of a kind
        return (3 << 10) + (val_count.index(3) << 2) + get_best_high(val_int)
    elif vc_hist[2] == 2:               # two pair
        return (2 << 10) + ((12 - val_count[::-1].index(2)) << 2) + val_count.index(2) + min(val_int)
    elif vc_hist[2] == 1:               # one pair
        return (1 << 10) + (val_count.index(2) << 2) + get_best_high(val_int)
    else:
        return get_best_high(val_int)

## encode the sorted value
def get_best_high(value):
    val_enc = [v << i for (i,v) in enumerate(sorted(value))]
    return sum(val_enc)

## returns the highest value in straight, or -1 if not straight
## 'value' in order form, not hand form
def get_straight(value):
    v = min(value)
    if min(value) == 0 and max(value) == 12: # if the highest value is Ace, ace = -1
        v = -1
    for i in sorted(value)[1:]:
        if i == v+1:
            v = i
        else:
            return -1
    return v

## return 1 if flush, -1 if not
def get_flush(suit):
    res = 1 if suit.count(suit[0]) == 5 else -1
    return res

def load_data():
    data_file = open('prob054_poker.txt', newline='\n')
    row = csv.reader(data_file, delimiter=' ')
    return [r for r in row]

if __name__ == "__main__":
    print(compute())