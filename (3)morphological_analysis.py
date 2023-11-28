

import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def morphological_analysis(sentence):
    tokens = word_tokenize(sentence)
    tagged_words = pos_tag(tokens)

    return tagged_words

# Example usage
sentence = "Unhappily, she ran quickly"
result = morphological_analysis(sentence)
print(result)

