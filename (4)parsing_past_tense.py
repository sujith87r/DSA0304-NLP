
import re

def parse_sentence(sentence):
    fsm = {'s': {'she': 'V1', 'he': 'V1'},
           'V1': {'walked': 'VPast', 'jumped': 'VPast', 'ran': 'VPast',
                  'played': 'VPast', 'ate': 'VPast', 'slept': 'VPast', 'sang': 'VPast'},
           'VPast': {'to': 'PREP', 'over': 'PREP'},
           'PREP': {'the': 'N', 'park': 'N', 'fence': 'N'},
           'N': {'yesterday': 'END'}}

    tokens = re.findall(r'\w+', sentence.lower())
    current_state = 's'

    for token in tokens:
        if current_state not in fsm or token not in fsm[current_state]:
            raise ValueError(f"Invalid token '{token}' in sentence '{sentence}'")
        else:
            current_state = fsm[current_state][token]

    if current_state != 'END':
        raise ValueError(f"Incomplete sentence: '{sentence}'")

def generate_past_tense(verb):
    if verb in {'walk', 'play', 'run'}:
        past_tense = verb + 'ed'
    elif verb in {'eat', 'sleep', 'sing'}:
        past_tense = verb + 't'
    else:
        raise ValueError(f"Unknown verb: '{verb}'")

    return past_tense

def test_specific_sentences():
    sentences_to_test = [
        "She walked to the park yesterday",
        "He jumped over the fence"
    ]

    for sentence in sentences_to_test:
        try:
            parse_sentence(sentence)
            print(f"Valid sentence: '{sentence}'")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    test_specific_sentences()