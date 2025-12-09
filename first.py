def count_words(sentence):
    num_characters = len(sentence)
    num_words = len(sentence.split())
    vowels = "aeiouAEIOU"
    num_vowels = 0
    for char in sentence:
        if char in vowels:
            num_vowels += 1
    return num_characters, num_words, num_vowels
sentence=input("enter a sentence:")
characters, words, vowels = count_words(sentence)
print("characters:", characters)
print("words :", words)
print("vowels:" , vowels)
