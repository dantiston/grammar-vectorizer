#!/usr/bin/env python3.7


from enum import Enum

from pyrsistent import freeze


class PartOfSpeech(Enum):

    ADJ, ADP, ADV, AUX, CCONJ, DET, INTJ, NOUN, NUM, PART, PRON, PROPN, PUNCT, SCONJ, SYM, VERB, X = range(1, 18)


class LexicalTypes(Enum):

    ADJ, COP, CONJ, DET, NOUN, PRON, VERB = range(1, 8)


POS_TO_TYPES = freeze({
    PartOfSpeech.ADJ.name: LexicalTypes.ADJ.name.lower(),
    PartOfSpeech.CCONJ.name: LexicalTypes.CONJ.name.lower(),
    PartOfSpeech.DET.name: LexicalTypes.DET.name.lower(),
    PartOfSpeech.NOUN.name: LexicalTypes.NOUN.name.lower(),
    PartOfSpeech.PRON.name: LexicalTypes.NOUN.name.lower(),
    PartOfSpeech.PROPN.name: LexicalTypes.NOUN.name.lower(),
    PartOfSpeech.VERB.name: LexicalTypes.VERB.name.lower(),
})
