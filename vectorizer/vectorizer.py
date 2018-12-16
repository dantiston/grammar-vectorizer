#!/usr/bin/env python3.7

from choices import Choices

class Vectorizer(object):

    def treebank_to_choices(self, treebank) -> Choices:
        result = Choices()
        result = result.update(self.treebank_to_lexicon())
        return result

    def treebank_to_lexicon(treebank) -> Choices:
        result = Choices()
        return result
