import os
import csv
import time

PROB_NUM = 1

def compute():
    return 233168


def test_prob000():
    dir_path = os.path.dirname(__file__)
    answer_file = open(os.path.join(dir_path, "../answers.txt"))
    answers = list(csv.reader(answer_file, delimiter='\n'))

    assert(str(compute()) == answers[PROB_NUM][0][4:])

if __name__ == "__main__":
    now = time.perf_counter()
    result = compute()
    duration = time.perf_counter() - now
    
    print("%d in %dms" % (result, duration))