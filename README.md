# Wordle Mini-Project (CSC 101)

## Assignment Goal

In this assignment, you will implement a simplified Wordle-style game in Python.
The emphasis is on understanding how strings, lists, loops, and functions work together to form a complete program.

The game rules are intentionally simplified so that the focus stays on clarity and reasoning rather than edge cases.

---

## Provided Data

### WORDS

Type: list of strings

This list contains all valid words used by the game.
Each word:

* is exactly five letters long
* uses only lowercase letters

The secret word is chosen from this list.

---

## Function Specifications

You must implement the following functions exactly as described.

---

### score_guess(guess, secret)

**Parameters**

* guess: a string representing the player’s guess
* secret: a string representing the secret word

**Returns**

* a string of length five made up of the characters Y, O, and X

**Behavior**

This function compares a guess to the secret word and produces feedback.
The returned string summarizes how well the guess matches the secret, one character per letter in the guess.

Each position in the result corresponds to the same position in the guess.
A character in the result indicates whether the guessed letter is a perfect match, a partial match, or not a match under the simplified game rules.

---

### is_valid_guess(guess)

**Parameters**

* guess: a string

**Returns**

* True if the guess is formatted correctly
* False otherwise

**Behavior**

This function checks whether the guess is a valid input for the game.
A valid guess has exactly five characters and contains only lowercase letters.

This function does not check whether the word appears in the word list.

---

### choose_secret(words)

**Parameters**

* words: a list of strings

**Returns**

* a string

**Behavior**

This function selects the secret word for the game.
For this assignment, the selected word is always the first element of the list.

This deterministic choice makes the game easier to test and grade.

---

### play_turn(secret, guess)

**Parameters**

* secret: a string representing the secret word
* guess: a string representing the player’s guess

**Returns**

* a string

**Behavior**

This function represents a single turn of the game.

If the guess is not valid, the function returns an error message.
If the guess is valid, the function returns feedback describing how the guess compares to the secret word.

---

### play_game(words)

**Parameters**

* words: a list of strings

**Returns**

* nothing

**Behavior**

This function runs the full game.

It selects a secret word, repeatedly asks the user for guesses, displays feedback, and stops when the player wins or runs out of guesses.

All user interaction happens in this function.

---

## Simplifications

This assignment does not fully implement official Wordle rules.
Duplicate-letter handling is simplified, and feedback is based only on letters appearing later in the secret word.

These choices are intentional and allow the logic to remain easy to understand and trace.


## Unit Tests

Make sure the provided Unit Tests Pass

Also write 1 unittest for each function, not play_game

