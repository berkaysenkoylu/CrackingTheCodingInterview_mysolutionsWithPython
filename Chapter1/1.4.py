## Chapter 1 - 1.4) Palindrome Permutation

from itertools import permutations

def isPalindrome(string):
    """A function that checks if the given string is a palindrome."""
    inverse_string = string[::-1]
    return string == inverse_string


def space_remover(string):
    """
    Removes the spaces from the given strings,
    but save the index numbers to a list,
    just in case!
    """
    newStr = ""
    space = []
    
    for i in range(len(string)):
        if string[i] != " ":
            newStr += string[i]
        else:
            space.append(i)
            
    return newStr, space


def space_inserter(string, indices):
    """Inserts spaces to specified locations!"""
    if len(indices) == 0:
        return string
    
    newStr = ""
    letters = [letter for letter in string]
    
    for index in indices:
        letters.insert(index, " ")
        
    return "".join(letters)


def permutation(string):
    """
    Function that checks if the permutations
    of the given string are palindromes!
    """
    ## Remove spaces in the string and save the indices for later use
    string, indices = space_remover(string)

    ## Get permutations, they are in letters, so you need to combine them!
    permutations_ = permutations(string, len(string))
    permutations_ = list(permutations_)
    
    ## Combine the letters to form words:
    words = []
    for word in permutations_:
        words.append(''.join(word))

    ## Check the permutations to see if they are palindrome! If so, add them to a list!
    palindromes = []
    for word in words:
        if isPalindrome(word) and word not in palindromes:
            palindromes.append(word)

    ## If the given string has a space or spaces, insert spaces in the actual locations and add them to a list
    ## then output the list! If spaces don't matter just output the "palindromes" list!
    words_to_output = [space_inserter(palindrome, indices) for palindrome in palindromes]

    return words_to_output


print permutation("tact coa")
