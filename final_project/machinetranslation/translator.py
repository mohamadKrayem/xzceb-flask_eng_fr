"""
This module provides access to the MyMemoryTranslator API 
for translation from English to French and vice versa.
"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    This function translates English text to French text.
    """
    translator = MyMemoryTranslator(source='en', target='fr')
    french_text = translator.translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    This function translates French text to English text.
    """
    translator = MyMemoryTranslator(source='fr', target='en')
    english_text = translator.translate(french_text)
    return english_text
