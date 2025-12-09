Word Counter with String Processing

This Python program reads a sentence from the user and counts the following:

Number of characters

Number of words

Number of vowels (a, e, i, o, u — both lowercase and uppercase)

Usage

Run the program.

Enter a sentence when prompted.

View the displayed results (characters, words, vowels).

Implementation

The main logic is in the count_words(sentence) function, which returns a 3-tuple:
(num_chars, num_words, num_vowels)

Vowels are defined using a Python set for efficient membership testing.

Words are counted using sentence.split(), which splits based on whitespace.

Example

Input:

Enter a sentence: Hello world! This is a test.


Output:

=== Results ===
Number of characters: 31
Number of words: 6
Number of vowels: 8
