#!/usr/bin/env python3.7

from pyrsistent import m


class Choices(object):


    def __init__(self, data={}):
        self.data = m(**data)


    def add(self, key, value) -> 'Choices':
        return Choices(self.data.set(key, value))


    def remove(self, key) -> 'Choices':
        return Choices(self.data.remove(key))


    def update(self, data) -> 'Choices':
        return Choices(self.data.update(data))


    def __str__(self):
        return str(self.data)


    def __repr__(self):
        return repr(self.data)[5:-1]


    def __get__(self, key: str):
        return self.data[key]


    def __eq__(self, value):
        if type(value) != Choices:
            return False
        return self.data == value.data
