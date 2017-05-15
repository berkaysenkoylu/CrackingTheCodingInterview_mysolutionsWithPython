## Chapter 1 - 1.2) Check Permutation

from itertools import permutations

def get_permutations(s1):
    permutations_ = permutations(s1, len(s1))
    permutations_ = list(permutations_)

    ## Get rid of the non-unique elements:
    b = []
    for ele in permutations_:
        if ele not in b:
            b.append(ele)

    ## Combine the letters to form words:
    words = []
    for word in b:
        words.append(''.join(word))

    return words

def compare_the_strings(s1, s2):
    my_list = get_permutations(s1)
    if s2 in my_list:
        return True
    else:
        return False


print compare_the_strings("berkay", "beryka")
