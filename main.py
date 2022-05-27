# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    word = str(word).lower().strip()
    anagram = str(anagram).lower().strip()
    
    if len(word) != len(anagram):
        return False
    elif sorted(word) == sorted(anagram):
        return True
    else:
        return False

word1 = " listen "
word2 = "SILENT"
print(find_anagram(word1, word2))

