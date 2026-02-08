import random

# ----- Word list (small on purpose) -----
WORDS = [
    "crane", "trace", "slate", "flame", "blame",
    "grape", "plane", "brick", "pride", "shine",
    "stone", "money", "cigar", "reign", "sweet",
    "sound", "round", "heart", "earth", "water"
]


# ----- Core scoring logic -----
def score_guess(guess, secret):
    result = []
    for i in range (5):
        if guess[i] == secret[i]:
            result.append("Y")
        elif guess[i] in secret[i+1: ]:
            result.append("O")
        else:
            result.append("X")
    return "".join(result)


# ----- Check guess formatting -----
def is_valid_guess(guess):
    if len(guess) != 5  and guess != str:
        return False
    
    for letter in guess:
        if letter < "a" or letter > "z":
            return False
        
    return True
# ----- Choose secret word -----
def choose_secret(words):
   return words[0]



# ----- One turn of the game -----
def play_turn(secret, guess):
    if is_valid_guess(guess) == False:
        return ("Invalid guess")
    return score_guess(guess, secret)


# ----- Full Wordle game -----
def play_game(words):
    secret = choose_secret(words)
    
    for x in range(6):
        guess = input("Enter a 5 letter word: ")
        turn_result = play_turn(secret, guess)
        print(turn_result)

        if turn_result == "YYYYY":
            print("You win!")
            return 
    print("You are out of guesses")
    print("The secret word is: ", secret)