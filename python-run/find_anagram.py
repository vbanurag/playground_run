from collections import Counter

def find_anagram_in_string(main_word, word_list, target_string):
    # Function to check if two words are anagrams
    def are_anagrams(word1, word2):
        return Counter(word1) == Counter(word2)

    # Function to find all substrings of a given length in the target string
    def get_substrings(string, length):
        return [string[i:i+length] for i in range(len(string) - length + 1)]

    # Iterate through each word in the word list
    for word in word_list:
        # Check if the word is an anagram of the main word
        if are_anagrams(main_word, word):
            # Get all substrings of the target string with the same length as the word
            substrings = get_substrings(target_string, len(word))
            print(substrings)

            # Check if any substring is an anagram of the word
            for substring in substrings:
                if are_anagrams(word, substring):
                    return word

    # If no anagram is found, return None
    return None

# Example usage
main_word = "listen"
word_list = ["silent", "hello", "world", "enlist"]
target_string = "The cat is very ntlise"

result = find_anagram_in_string(main_word, word_list, target_string)
print(f"Word from the list whose anagram is in the string: {result}")
