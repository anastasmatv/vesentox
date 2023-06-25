def is_anagram(word1, word2):
    sorted_word1 = sorted(word1.lower())
    sorted_word2 = sorted(word2.lower())
    if sorted_word1 == sorted_word2:
        return True
    else:
        return False

print(is_anagram("listen", "silent"))
print(is_anagram("hello", "world"))
