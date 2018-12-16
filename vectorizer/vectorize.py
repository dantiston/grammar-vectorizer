#!/usr/bin/env python3.7

from conllu import parse_tree

from choices import Choices
from vectorizer import Vectorizer


def vectorize(args) -> Choices:
    with open(args.treebank, 'r') as f:
        treebank = parse_tree(f)
    return Vectorizer().treebank_to_choices(treebank)


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser("Generate a choices file from a Universal Dependencies treebank")
    parser.add_argument("treebank", type=str, help="path to a Universal Dependencies conllu file")

    args = parser.parse_args()

    choices = vectorize(args)
    print(choices)
