# ez_address/cli.py
from __future__ import annotations

import argparse
from .macutil import normalize, classify, random_laa

def main() -> int:
    p = argparse.ArgumentParser(prog="ez_address")
    sub = p.add_subparsers(dest="cmd", required=True)

    p_norm = sub.add_parser("normalize")
    p_norm.add_argument("mac")

    p_class = sub.add_parser("classify")
    p_class.add_argument("mac")

    p_rand = sub.add_parser("random")
    p_rand.add_argument("--prefix", default=None)

    args = p.parse_args()

    if args.cmd == "normalize":
        print(normalize(args.mac))
    elif args.cmd == "classify":
        print(classify(args.mac))
    elif args.cmd == "random":
        print(random_laa(args.prefix))
    return 0
