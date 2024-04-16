import spacy
text = input("Enter a text: ")
language = input("Enter the language code (e.g., 'fr' for French, 'de' for German): ")
nlp = spacy.blank(language)
doc = nlp(text)
sentences = [sent.text for sent in doc.sents]
# Print the tokenized sentences
print("\nTokenized sentences:")
for idx, sentence in enumerate(sentences, start=1):
    print(f"Sentence {idx}: {sentence}")
