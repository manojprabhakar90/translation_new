**Translation Package**
**Overview**
This package provides a translation service using the facebook/mbart-large-50-many-to-many-mmt model. It supports translating text between multiple languages, including automatic language detection. This is useful for integrating translation capabilities into your applications.

**Features**                                             
Multi-language translation: Supports 50+ languages.
Automatic language detection: Detects the language of the input text.
Uses facebook/mbart-large-50-many-to-many-mmt model: State-of-the-art multilingual translation model.
Simple API: Easy integration into your Python projects.
Installation
Using Poetry
If you're using Poetry to manage dependencies, follow these steps:

**Clone this repository:**

bash:  git clone https://github.com/username/translation-package.git
cd translation-package
Install dependencies with Poetry:
poetry install

git clone https://github.com/username/translation-package.git
Install the dependencies:

bash
pip install -r requirements.txt
**Usage:**
from translation.translator import Translator

# Initialize translator
translator = Translator()

# Translate a sentence
translated_text = translator.translate("Hello, how are you?", lang="fr")
print(translated_text)  # Outputs: "Bonjour, comment ça va ?"

translated_text = translator.translate("Hola, ¿cómo estás?", lang="auto")
print(translated_text)  # Outputs: "Hello, how are you?"
Supported Languages
This package supports translation between the following languages (identified by their ISO codes):

Arabic (ar)
Bengali (bn)
Chinese (zh)
French (fr)
German (de)
Hindi (hi)
Spanish (es)
And many more!
For a complete list of supported languages, please check the LANGUAGE_CODES in the Translator class.

Running Tests
You can run the tests using pytest to ensure everything is working:

Install pytest:

bash
pip install pytest
Run the tests:

bash
pytest

Contributing
We welcome contributions to improve the translation package. If you'd like to contribute:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Push to the branch (git push origin feature-branch).
Create a pull request with a description of your changes.
License
This project is licensed under the MIT License - see the LICENSE file for details.
