
import nltk
from nltk.stem import PorterStemmer

nltk.download('punkt')

def apply_porter_stemmer(word_list):
    porter = PorterStemmer()
    stemmed_words = [porter.stem(word) for word in word_list]
    return stemmed_words

# Example usage
words_before_stemming = ["jumps", "jumping", "jumper", "jumped", "easily", "running", "flies", "flying", "flies"]

words_after_stemming = apply_porter_stemmer(words_before_stemming)

# Print before and after stemming
for before, after in zip(words_before_stemming, words_after_stemming):
    print(f"Before: {before}\tAfter: {after}")