# from .exceptions import *
import random
LIST_OF_WORDS = []

def _get_random_word(list_of_words):
    return random.choice(list_of_words)

def _mask_word(word):
    return '*'*len(word) 

def _uncover_word(answer_word, masked_word, letter):
    return ''.join(
        letter if answer_word[i] == letter else masked_letter
        for i, masked_letter in enumerate(masked_word)
    )

def guess_letter(game, letter):
        new_masked_word = _uncover_word(game['answer_word'], game['masked_word'], letter)
        if game['masked_word'] == new_masked_word:
            game['remaining_misses'] -= 1
        else:
            game['masked_word'] = new_masked_word
        
        game['previous_guesses'].append(letter)

def start_new_game(list_of_words=None, number_of_guesses=5):
    if list_of_words is None:
        list_of_words = LIST_OF_WORDS

    word_to_guess = _get_random_word(list_of_words)
    masked_word = _mask_word(word_to_guess)
    game = {
        'answer_word': word_to_guess,
        'masked_word': masked_word,
        'previous_guesses': [],
        'remaining_misses': number_of_guesses,
    }

    return game
