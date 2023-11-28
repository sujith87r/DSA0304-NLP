import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import BrillTaggerTrainer
from nltk.tag.brill import BrillTagger

nltk.download('punkt')
nltk.download('brown')
nltk.download('universal_tagset')

def train_brill_tagger(tagged_corpus):
    baseline_tagger = nltk.UnigramTagger(tagged_corpus)
    templates = nltk.tag.brill.fntbl37()
    trainer = BrillTaggerTrainer(baseline_tagger, templates)
    brill_tagger = trainer.train(tagged_corpus, max_rules=10)

    return brill_tagger

def stochastic_pos_tagging(text, tagger):
    words = word_tokenize(text)
    tagged_words = tagger.tag(words)
    return tagged_words

# Example usage
sentences = [
    "The red car stopped at the traffic light",
    "She quickly ran to catch the bus"
]

# Training the BrillTagger on the Brown corpus (you can use a larger corpus for better performance)
tagged_corpus = nltk.corpus.brown.tagged_sents(tagset='universal')
brill_tagger = train_brill_tagger(tagged_corpus)

# Stochastic part-of-speech tagging for each sentence
for sentence in sentences:
    tagged_sentence = stochastic_pos_tagging(sentence, brill_tagger)
    print(f"Original Sentence: {sentence}")
    print("Stochastic POS Tagging:", tagged_sentence)
    print()