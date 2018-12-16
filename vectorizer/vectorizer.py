#!/usr/bin/env python3.7


from choices import Choices

from pyrsistent import s

class Vectorizer(object):

    def treebank_to_choices(self, treebank) -> Choices:
        result = Choices()
        result = result.merge(self.treebank_to_lexicon(treebank))
        return result

    def treebank_to_lexicon(self, treebank) -> Choices:
        result = set()
        for sentence in treebank:
            result.add(sentence.token['lemma'].lower()) # add root
        return Choices({"lexicon": s(*result)})
