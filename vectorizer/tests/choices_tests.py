#!/usr/bin/env python3.7


import unittest

from choices import Choices


class ChoicesInitTests(unittest.TestCase):

    def test_basic(self):
        Choices({"abc": "def"})

    def test_empty(self):
        Choices()


class ChoicesAddTests(unittest.TestCase):

    def test_basic(self):
        actual = Choices().add("abc", "def")
        expected = Choices({"abc": "def"})
        self.assertEqual(actual, expected)


    def test_existing_keys(self):
        actual = Choices({"abc": "def"}).add("xyz", "zyx")
        expected = Choices({"abc": "def", "xyz": "zyx"})
        self.assertEqual(actual, expected)


    def test_replacing(self):
        actual = Choices({"abc": "abc"}).add("abc", "def")
        expected = Choices({"abc": "def"})
        self.assertEqual(actual, expected)
