#!/usr/bin/env python3.7


from typing import Any, Dict, Mapping
from enum import Enum

from pyrsistent import freeze


class Choices(object):

    class Section(Enum):
        General = 'general'
        WordOrder = 'word-order'
        Number = 'number'
        Person = 'person'
        Gender = 'gender'
        Case = 'case'
        DirectInverse = 'direct-inverse'
        TenseAspectMood = 'tense-aspect-mood'
        Other = 'other-features'
        SententialNegation = 'sentential-negation'
        Coordination = 'coordination'
        MatrixYesNo = 'matrix-yes-no'
        InformationStructure = 'info-str'
        ArgumentOptionality = 'arg-opt'
        Lexicon = 'lexicon'
        Morphology = 'morphology'

        def __init__(self, friendly_name):
            self.friendly_name = friendly_name

        def __str__(self):
            return self.friendly_name


    def __init__(self, data: Dict={}):
        self.data: Dict = freeze(data)


    def add(self, key: Section, value) -> 'Choices':
        return Choices(self.data.set(key, value))


    def remove(self, key: Section) -> 'Choices':
        return Choices(self.data.remove(key))


    def update(self, data: Mapping[Section, Any]) -> 'Choices':
        return Choices(self.data.update(data))


    def merge(self, other: 'Choices') -> 'Choices':
        return self.update(other.data)


    def sections(self):
        return self.data.keys()


    def __str__(self):
        # TODO: This is wholly inadequate
        result = []
        for section in Choices.Section:
            subresult = [f"section={section}"]
            if section in self:
                for datum in self[section]:
                    subresult.append(f"\t{datum}")
            result.append("\n".join(subresult))
        return "\n\n".join(result)


    def __contains__(self, key: Section):
        return key in self.data


    def __repr__(self):
        return repr(self.data)[5:-1]


    def __getitem__(self, key: str):
        return self.data[key]


    def __eq__(self, value):
        if type(value) != Choices:
            return False
        return self.data == value.data
