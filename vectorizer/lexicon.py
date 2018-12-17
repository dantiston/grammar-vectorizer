#!/usr/bin/env python3.7


from collections import defaultdict
from typing import Mapping, Set, Tuple

from lemma import Lemma
from constants import POS_TO_TYPES

from pyrsistent import freeze


class LexiconBuilder(object):

    def __init__(self):
        self.lemma_to_entry = defaultdict(set)


    def consider(self, token) -> None:
        pos = token['upostag']
        if pos in POS_TO_TYPES:
            lemma = token['lemma']
            form = token['form']
            self.lemma_to_entry[(lemma, pos)].add(form)


    def finalize(self) -> Lexicon:
        form_to_entry = self._build_form_to_entry()
        lemma_to_entry = self._build_lemma_to_entry(form_to_entry)
        return Lexicon(form_to_entry, lemma_to_entry)


    def _build_form_to_entry(self) -> Mapping[Tuple[str, str], Lemma]:
        return {(form, pos): Lemma.of(lemma, pos, tokens) for (lemma, pos), tokens in self.lemma_to_entry.items()}


    def _build_lemma_to_entry(self, form_to_entry: Mapping[Tuple[str, str], Lemma]) -> Mapping[Tuple[str, str], Lemma]:
        return {(lemma, pos): Lemma.of(lemma, pos, tokens) for (lemma, pos), tokens in self.lemma_to_entry.items()}


@dataclass
class Lexicon(object):

    form_to_entry: Mapping[Tuple[str, str], Lemma]
    lemma_to_entry: Mapping[Tuple[str, str], Lemma]

    @staticmethod
    def of(form_to_entry: Mapping[Tuple[str, str], Lemma], lemma_to_entry: Mapping[Tuple[str, str], Lemma]):
        return Lexicon(freeze(form_to_entry), freeze(lemma_to_entry))
