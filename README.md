# Word Counter with String Processing

## Objective  
This simple Python program reads a sentence (string) from the user, and counts:
- Number of characters  
- Number of words  
- Number of vowels (a, e, i, o, u — both lowercase and uppercase)  

## Usage  
1. Clone the repository.  
2. Run python word_counter.py (or whatever you name the file).  
3. Enter a sentence when prompted.  
4. View the displayed results (characters, words, vowels).

## Implementation  
- The main logic is in count_words(sentence) function, which returns a 3-tuple (num_chars, num_words, num_vowels).  
- The vowels are defined using a Python set for efficient membership testing.  
- Word splitting is done by sentence.split() so words are counted based on whitespace separation.

## Example  

Enter a sentence: Hello world! This is a test.
=== Results ===
Number of characters: 31
Number of words:      6
Number of vowels:     8

