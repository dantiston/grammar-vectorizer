#!/usr/bin/env python3.7

"""Utilities for working with token graphs, such as dependency parses"""

from typing import Iterable, List, Mapping


def get_tokens_from_root(root) -> List[Mapping[str, str]]:
    result = [root.token]
    for child in root.children:
        result.extend(get_tokens_from_root(child))
    return result


def iter_tokens_from_root(root) -> Iterable[Mapping[str, str]]:
    yield root.token
    for child in root.children:
        yield from iter_tokens_from_root(child)
