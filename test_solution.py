import unittest

from solution import reverse_string, count_vowels


class TestReverseString(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_empty(self):
        self.assertEqual(reverse_string(""), "")

    def test_single_char(self):
        self.assertEqual(reverse_string("a"), "a")

    def test_palindrome(self):
        self.assertEqual(reverse_string("madam"), "madam")

    def test_spaces_and_case(self):
        self.assertEqual(reverse_string("Hello World"), "dlroW olleH")


class TestCountVowels(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(count_vowels("Hello World"), 3)

    def test_empty(self):
        self.assertEqual(count_vowels(""), 0)

    def test_uppercase(self):
        self.assertEqual(count_vowels("AEIOU"), 5)

    def test_mixed_case(self):
        self.assertEqual(count_vowels("aEiOu"), 5)

    def test_no_vowels(self):
        self.assertEqual(count_vowels("rhythm"), 0)


if __name__ == "__main__":
    unittest.main()
