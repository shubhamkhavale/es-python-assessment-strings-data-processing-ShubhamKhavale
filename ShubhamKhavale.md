# Python Programming Assessment: Strings & Data Processing

**Company:** Embed Square Solutions Private Limited
**Role:** Python Developer Intern

- **Full Name:** YOUR FULL NAME
- **Submission Date:** 19 October 2026

## Files

| File | Description |
|------|-------------|
| `solution.py` | Implementation of `reverse_string` and `count_vowels` |
| `test_solution.py` | Unit tests covering normal inputs and edge cases |

## Approach

### 1. `reverse_string(text: str) -> str`
I loop through the string from the last index to the first
(`range(len(text) - 1, -1, -1)`) and append each character to a new string.
An empty string simply returns an empty string.

### 2. `count_vowels(text: str) -> int`
I iterate over each character, convert it to lowercase with `.lower()`, and
check whether it is in `"aeiou"`. This handles both uppercase and lowercase
vowels. An empty string returns `0`.

## How to Run

```bash
python solution.py
python -m unittest test_solution.py -v
```

## Sample Output

```
olleh
3
```
