import os
import argparse
import importlib


if __name__ == "__main__":
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '-p', '--prob', type=int, required=True, help='project euler problem number',
    )
    parser.add_argument(
        '-l', '--lang', default="py", choices=["py", "cpp", "rust"], help='language backend',
    )
    args = parser.parse_args()

    probnum = 'prob' + ('0' * (3-len(str(args.prob)))) + str(args.prob)

    if args.lang is "python":
        import py
        
        prob = importlib.import_module("py." + probnum)
        print(prob.compute())
        