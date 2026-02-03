import unittest

# import everything from the wordle file
# if the file is named wordle.py:
from p2 import (
    score_guess,
    is_valid_guess,
    choose_secret,

    play_turn,
    WORDS
)


class TestScoreGuess(unittest.TestCase):

    def test_all_correct(self):
        self.assertEqual(score_guess("crane", "crane"), "YYYYY")

    def test_no_letters(self):
        self.assertEqual(score_guess("crane", "brick"), "OYXXX")

    def test_mixed_result(self):
        # c r a n e
        # t r a c e
        # X Y Y O Y
        self.assertEqual(score_guess("crane", "trace"), "OYYXY")

    def test_late_occurrence_only(self):
        # 'a' only appears later
        self.assertEqual(score_guess("abcde", "eabcd"), "OOOOX")


class TestIsValidGuess(unittest.TestCase):

    def test_valid_guess(self):
        self.assertTrue(is_valid_guess("crane"))

    def test_too_short(self):
        self.assertFalse(is_valid_guess("cat"))

    def test_too_long(self):
        self.assertFalse(is_valid_guess("kittens"))

    def test_non_letters(self):
        self.assertFalse(is_valid_guess("a1cde"))
        self.assertFalse(is_valid_guess("ab-de"))


class TestChooseSecret(unittest.TestCase):

    def test_choose__word(self):
        words = ["apple", "brick", "crane"]
        self.assertIn(choose_secret(words), "apple")


class TestPlayTurn(unittest.TestCase):

    def test_invalid_guess(self):
        self.assertEqual(play_turn("crane", "cat"), "Invalid guess")

    def test_valid_guess(self):
        self.assertEqual(play_turn("crane", "crane"), "YYYYY")


if __name__ == "__main__":
    unittest.main()

