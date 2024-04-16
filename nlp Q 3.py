########Write a Python NLTK program to get a list of common stop words in various languages
#in Python.
import nltk
# Get list of languages
languages = nltk.corpus.stopwords.fileids()
# Create a dictionary to store stopwords for each language
stopwords_languages = {}
# Get stopwords for each language
for lang in languages:
    stopwords = nltk.corpus.stopwords.words(lang)
    stopwords_languages[lang] = stopwords
for lang, stopwords in stopwords_languages.items():
    print(f"\nStopwords for {lang}:")
    print(stopwords)

