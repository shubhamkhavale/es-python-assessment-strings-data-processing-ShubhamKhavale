"""Python Programming Assessment: Strings & Data Processing
Embed Square Solutions Private Limited - Python Developer Intern
"""


def reverse_string(text: str) -> str:
    """Return the reverse of the given string.

    Walks through the string from the last index to the first
    and builds the reversed string character by character.
    """
    reversed_text = ""
    for i in range(len(text) - 1, -1, -1):
        reversed_text += text[i]
    return reversed_text


def count_vowels(text: str) -> int:
    """Return the number of vowels (a, e, i, o, u) in the string.

    Both uppercase and lowercase vowels are counted.
    """
    vowels = "aeiou"
    count = 0
    for char in text:
        if char.lower() in vowels:
            count += 1
    return count


if __name__ == "__main__":
    print(reverse_string("hello"))       # olleh
    print(count_vowels("Hello World"))   # 3
