from .exceptions import *
import random
LIST_OF_WORDS = ['INE','SDA','Python','Exceptions','Code']

def _get_random_word(list_of_words):
    if not list_of_words:
        raise InvalidListOfWordsException()
    return random.choice(list_of_words)

def _mask_word(word):
    if not word:
        raise InvalidWordException()
    return '*'*len(word) 

def _uncover_word(answer_word, masked_word, letter):
    if (not answer_word) or (not masked_word) or (len(answer_word) != len(masked_word)):
        raise InvalidWordException()

    if len(letter) > 1:
        raise InvalidGuessedLetterException()

    return ''.join(
        letter if answer_word[i] == letter else masked_letter
        for i, masked_letter in enumerate(masked_word)
    )

def _is_game_finished(game):
    return game['answer_word'] == game['masked_word'] or game['remaining_misses'] <= 0
    
def guess_letter(game, letter):
    if _is_game_finished(game):
        raise GameFinishedException()

    letter = letter.lower()
    if letter in game['previous_guesses']:
        raise InvalidGuessedLetterException()

    game['previous_guesses'].append(letter)
    new_masked_word = _uncover_word(game['answer_word'], game['masked_word'], letter)

    if game['masked_word'] == new_masked_word:
        game['remaining_misses'] -= 1
    else:
        game['masked_word'] = new_masked_word
    
    if game['answer_word'] == game['masked_word']:
        raise GameWonException()
    elif game['remaining_misses'] <= 0:
        raise GameLostException()

def start_new_game(list_of_words=None, number_of_guesses=5):
    if list_of_words is None:
        list_of_words = LIST_OF_WORDS

    word_to_guess = _get_random_word(list_of_words).lower()
    masked_word = _mask_word(word_to_guess)
    game = {
        'answer_word': word_to_guess,
        'masked_word': masked_word,
        'previous_guesses': [],
        'remaining_misses': number_of_guesses,
    }

    return game
