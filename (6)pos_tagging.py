import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def pos_tagging(text):
    words = word_tokenize(text)
    tagged_words = pos_tag(words)
    return tagged_words

# Example usage
text1 = "The sun is shining brightly"
text2 = "I love reading interesting books"

tagged_text1 = pos_tagging(text1)
tagged_text2 = pos_tagging(text2)

print("POS tagging for text1:", tagged_text1)
print("POS tagging for text2:", tagged_text2)