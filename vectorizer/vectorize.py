#!/usr/bin/env python3.7

import argparse

from typing import Dict

from conllu import parse_tree

from choices import Choices
from vectorizer import Vectorizer


def gather_metadata(args: argparse.Namespace) -> Dict[str, str]:
    result = {"language": args.language}
    if 'iso_code' in args:
        result['iso-code'] = args.iso_code
    return result


def vectorize(args: argparse.Namespace) -> Choices:
    with open(args.treebank, 'r') as f:
        treebank = parse_tree(f.read())
    return Vectorizer().treebank_to_choices(treebank, gather_metadata(args))


if __name__ == "__main__":

    parser = argparse.ArgumentParser("Generate a choices file from a Universal Dependencies treebank")
    parser.add_argument("treebank", type=str, help="path to a Universal Dependencies conllu file")
    parser.add_argument("--language", required=True, type=str, help="name of the language")
    parser.add_argument("--iso-code", type=str, help="ISO code for the language")

    args = parser.parse_args()

    choices = vectorize(args)
    import pdb; pdb.set_trace()
    print(len(choices['lexicon']))
