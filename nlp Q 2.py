########Write a python program that take an input text from the user and apply part-of-speech
#tagging, and return back correct tags per word.
#Note: use two different tagset and compare the output.
import nltk
text = input("Enter a sentence: ")
words = nltk.word_tokenize(text)
tagged_words_penn = nltk.pos_tag(words)
tagged_words_universal = nltk.pos_tag(words, tagset='universal')
print("\nTagged words with Penn Treebank tagset:")
print(tagged_words_penn)
print("\nTagged words with Universal tagset:")
print(tagged_words_universal)
