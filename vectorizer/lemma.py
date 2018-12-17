#!/usr/bin/env python3.7


from dataclasses import dataclass
from typing import FrozenSet, Iterable

from constants import PartOfSpeech


CASE_SENSITIVE_TAGS = frozenset({PartOfSpeech.PROPN})


@dataclass(frozen=True)
class Lemma(object):

    lemma: str
    pos: str
    tokens: FrozenSet[str]

    def of(lemma: str, pos: str, tokens: Iterable[str]):
        if pos not in CASE_SENSITIVE_TAGS:
            tokens = map(str.lower, tokens)
        return Lemma(lemma, pos, frozenset(tokens))
