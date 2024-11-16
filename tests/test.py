import pytest
from translation.translator import Translator

def test_translation_french():
    translator = Translator()
    result = translator.translate("Hello, how are you?", lang="fr")
    assert result is not None

def test_translation_german():
    translator = Translator()
    result = translator.translate("Hello, how are you?", lang="de")
    assert result is not None

def test_translation_hindi():
    translator = Translator()
    result = translator.translate("Hello, how are you?", lang="hi")
    assert result is not None
