# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    # first we convert both the strings into lowercase
    word = word.lower()
    anagram = anagram.lower()

    # check if length is same
    if(len(word) == len(anagram)):

        # secondd step: we sort the strings
        sortedWord = sorted(word)
        sortedAnagram = sorted(anagram)

        # if sorted char arrays are same
        if(sortedWord == sortedAnagram):
            True     
        else:
            False       

        if True:
            print(word + " and " + anagram + " are anagrams.")
    else:
            print(word + " and " + anagram + " are not anagrams.")
        
        

find_anagram("below", "elbow")
