# coding: utf-8
# Problem: Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.
# Input: String="catfoxcat", Words=["cat", "fox"]
# Output: [0, 3]
# Explanation: The two substring containing both the words are "catfox" & "foxcat".
# Leetcode Equivalent: https://leetcode.com/problems/substring-with-concatenation-of-all-words/
# Optimal solution:

def findSubstring(s, words):

    # if the length of the words array is 0 or the length of the first word in words is 0
    # there must not exist a substring of s

    if len(words) == 0 or len(words[0]) == 0:
        return []

    # declare a hashmap to store the words in the array
    word_frequency = {}

    # iterate through each item in the words and make a hashmap
    for word in words:
        if word not in word_frequency:
            word_frequency[word] = 0
        word_frequency[word] += 1

    result_indices = []
    words_count = len(words)  # the number of items in the array
    word_length = len(words[0])  # the length of each of the words in the array

    for i in range((len(s) - words_count * word_length) + 1):  # iterating through till the
        words_seen = {}  # the dictionary of words that has been iterated through already
        for j in range(0, words_count):  # iterating through till the number of words
            # the next index is the (i + j)th index * word_length
            next_word_index = i + j * word_length
            # the word consists of the string s which is sliced as the beginning to end of the next word
            word = s[next_word_index: next_word_index + word_length]

            # if this word is not in the the word_frequency dictionary which consists of the og words
            if word not in word_frequency:
                # skip this word and go to the next
                break

            # if this words has not been seen then add it to the word that has been seen
            if word not in words_seen:
                words_seen[word] = 0
            words_seen[word] += 1

            # if this word has been seen more times than it occurs in the word_frequency dict
            if words_seen[word] > word_frequency.get(word, 0):
                break

            if j + 1 == words_count:
                result_indices.append(i)

    return result_indices


if __name__ == "__main__":
    print(findSubstring("wordgoodbest",
          ["word", "good", "best", "word"]))
