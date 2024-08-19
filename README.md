# Hangman Game
  *This project is part of the [INE](my.ine.com) x [SDA](https://t.co/zI6rJymObV) Data Science Program, [Exceptions with Python](https://my.ine.com/DataScience/courses/961cea55/exceptions-with-python).*

**Hangman Game** is a straightforward text-based game where players attempt to guess a hidden word one letter at a time. The game ends when the player either uncovers the entire word or runs out of attempts.

## Features

- **Mask Word**: Converts a given word into a masked format with asterisks.
- **Uncover Word**: Updates the masked word with the guessed letter if it is present in the word.
- **Get Random Word**: Selects a random word from a provided list of words.
- **Guess Letter**: Handles the game logic for guessing letters, including tracking attempts and determining win/loss conditions.


## Sample Run
```
=====================
###### Hangman ######
=====================
Enter your list of words separated by comma. Leave empty for default: 
Enter how the number of attempts allowed. Leave empty for default: 

### Game Initialized. Let's play!!

(******) Enter new guess (5 remaining attempts): p
        Congratulations! That's correct.

(p*****) Enter new guess (5 remaining attempts): y
        Congratulations! That's correct.

(py****) Enter new guess (5 remaining attempts): t 
        Congratulations! That's correct.

(pyt***) Enter new guess (5 remaining attempts): h
        Congratulations! That's correct.

(pyth**) Enter new guess (5 remaining attempts): o
        Congratulations! That's correct.

(pytho*) Enter new guess (5 remaining attempts): g
        :( That's a miss!

(pytho*) Enter new guess (4 remaining attempts): n
         YES! You win! The word was: python
```

