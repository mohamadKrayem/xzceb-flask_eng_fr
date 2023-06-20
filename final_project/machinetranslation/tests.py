import unittest
import translator 

class TestTranslatorEnglishToFrench(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(translator.english_to_french('Good Morning'), 'Bonjour')
        self.assertNotEqual(translator.english_to_french('Hello'), 'Hello')

class TestTranslatorFrenchToEnglish(unittest.TestCase):
    def test_french_to_english(self):
        self.assertEqual(translator.french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(translator.french_to_english('Bonjour'), 'Bonjour')

unittest.main()
