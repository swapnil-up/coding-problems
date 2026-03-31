# Topic: String Operations & Formatting
# Concepts: slicing, methods, f-strings, str.join, str.split, str.strip
#
# Python strings are immutable sequences. Most "mutations" return a new string.
# Key things to know:
#   - Slicing:      s[start:stop:step]  (negative indices count from end)
#   - Formatting:   f"{value!r}"  /  f"{number:.2f}"  /  f"{val:<10}"
#   - Useful methods: .split(), .join(), .strip(), .replace(), .startswith()
#
# Reference: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str


# --- Problem 1 ---
# Reverse a string without using reversed() or slicing tricks you don't understand.
# Example: reverse("hello") == "olleh"
def reverse(s: str) -> str:
    return s[len(s):-len(s)-1:-1]


# --- Problem 2 ---
# Given a sentence, return a list of words longer than n characters.
# Example: long_words("the quick brown fox", 3) == ["quick", "brown"]
def long_words(sentence: str, n: int) -> list[str]:
    words = sentence.split(" ")
    return [word for word in words if len(word)>n]
    


# --- Problem 3 ---
# Format a name and score into a fixed-width leaderboard row.
# Output must be exactly: "Alice          :  9420"
# (name left-aligned in 15 chars, score right-aligned in 6 chars)
def leaderboard_row(name: str, score: int) -> str:
    raise NotImplementedError("TODO")


# --- Problem 4 ---
# Given a CSV line (possibly with extra spaces around values), return a clean list.
# Example: parse_csv("  alice , 30 , engineer  ") == ["alice", "30", "engineer"]
def parse_csv(line: str) -> list[str]:
    raise NotImplementedError("TODO")


# --- Problem 5 ---
# Count how many times each vowel appears in a string (case-insensitive).
# Return a dict. Only include vowels that actually appear.
# Example: vowel_count("Hello World") == {"e": 1, "o": 2}
def vowel_count(s: str) -> dict[str, int]:
    raise NotImplementedError("TODO")


# ---- Tests ----
def run_tests():
    assert reverse("hello") == "olleh"
    assert reverse("a") == "a"
    assert reverse("") == ""

    assert long_words("the quick brown fox", 3) == ["quick", "brown"]
    assert long_words("hi", 5) == []

    assert leaderboard_row("Alice", 9420) == "Alice          :   9420"

    assert parse_csv("  alice , 30 , engineer  ") == ["alice", "30", "engineer"]
    assert parse_csv("x") == ["x"]

    assert vowel_count("Hello World") == {"e": 1, "o": 2}
    assert vowel_count("xyz") == {}

    print("strings.py: all tests passed!")


if __name__ == "__main__":
    run_tests()