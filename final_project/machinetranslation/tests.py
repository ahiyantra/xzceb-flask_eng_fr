import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour") # test when "Hello" is given as input & the output is "Bonjour"
        self.assertEqual(english_to_french("Goodbye"), "Au revoir") # test when "Goodbye" is given as input & the output is "Au revoir"

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello") # test when "Bonjour" is given as input & the output is "Hello"
        self.assertEqual(french_to_english("Au revoir"), "Goodbye") # test when "Au revoir" is given as input & the output is "Goodbye"

unittest.main()
