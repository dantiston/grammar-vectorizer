#!/usr/bin/env python3.7


from typing import Dict

import token_graph

from choices import Choices
from lexicon import Lexicon


class Vectorizer(object):

    def treebank_to_choices(self, treebank, metadata: Dict[str, str]) -> Choices:
        result = Choices()
        result = result.merge(self.metadata_to_choices(metadata))
        result = result.merge(self.treebank_to_lexicon(treebank))
        return result

    def treebank_to_lexicon(self, treebank) -> Choices:
        result = Lexicon()
        for sentence in treebank:
            for token in token_graph.iter_tokens_from_root(sentence):
                result.consider(token)
        return Choices({Choices.Section.Lexicon: {Lemma.of(lemma, pos, forms) for (lemma, pos), forms in result.items()}})

    def metadata_to_choices(self, metadata: Dict[str, str]) -> Choices:
        return Choices({Choices.Section.General: metadata})
