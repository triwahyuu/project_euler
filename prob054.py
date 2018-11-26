## it's not done
## the possible way of solving this is to make a scoring of the hand
## of each player, by encoding the category of winning and the cards
import csv

value = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
val_order = {(k, v) for v,k in enumerate(c)}

def compute():
    poker_hand = load_data()
    ans = sum(1 for x in poker_hand if who_wins(x) == 1)
    return ans

## returns who win the hand, 1:player1, 2:player2
def who_wins(hands):
    p1 = [(a[0], a[1]) for a in hands[:5]]  # (value, suit)
    p2 = [(a[0], a[1]) for a in hands[5:]]
    # count how many times a value occurs
    p1_val = [a[0] for a in p1]
    p2_val = [a[0] for a in p2]
    p1_val_count = dict((x, p1_val.count(x)) for x in set(p1_val))
    p2_val_count = dict((x, p2_val.count(x)) for x in set(p2_val))
    
    return 0

def load_data():
    data_file = open('prob054_poker.txt', newline='\n')
    row = csv.reader(data_file, delimiter=' ')
    return [r for r in row]

if __name__ == "__main__":
    hands = load_data()
    print(who_wins(hands[0]))
    # print(compute())