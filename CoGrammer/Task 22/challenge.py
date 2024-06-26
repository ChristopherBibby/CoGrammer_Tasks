# Code to complete the Little Sister's challenge

def add_prefix_un(word):
    return 'un' + word

def make_word_groups(vocab_words):
    return (' :: ' + vocab_words[0]).join(vocab_words)

def remove_suffix_ness(word):
    return word[:-4] if word[-5] != 'i' else word[:-5]+'y'

def adjective_to_verb(sentence, index):
    return sentence.split()[index].rstrip('.') + 'en'