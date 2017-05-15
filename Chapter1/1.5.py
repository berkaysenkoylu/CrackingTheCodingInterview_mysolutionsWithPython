## Chapter 1 - 1.5) One away

"""
There are three types of edits which can be done
to a string:
- Remove
- Insert
- Replace

The main point is to do these edits on a string once separately
and get all the combinations in a list. Then, check if the
other string is in the list.
"""

def removeFromString(string, lst):
    for i in range(len(string)):
        str_ = ""
        if i == 0:
            str_ += string[i+1:]
        else:
            str_ += string[:i] + string[i+1:]
        lst.append(str_)
    return lst
            
        
def isInserted(s1, s2):
    """
    A function that checks the letter difference
    it must be 1 at most! Note that lengths of the
    given strings are different! I assumed that
    len(s2) > len(s1), which can be changed.
    """
    s1_list = list(s1)
    s2_list = list(s2)
    count = 0
    
    if abs(len(s1) - len(s2)) != 1:
        return False
    else:
        for letter in s1_list:
            if letter in s2_list:
                count += 1
        if count == len(s1):
            return True
        else:
            return False


def letterDifference(s1, s2):
    """The number of different letters must be 1 at most!"""
    count = 0
    for x, y in zip(s1, s2):
        if x != y:
            count += 1
    
    if count == 1:
        return True
    else:
        return False


def oneWay(s1, s2):
    """Main function"""
    ## Form combinations for "Remove" case.
    ## I remove every possible letter once and form
    ## a new string, then add it to a list.
    removal_combs = []
    removeFromString(s1, removal_combs)
    
    if len(s1) == len(s2):
        ## "Replace" case:
        return letterDifference(s1, s2)
    elif len(s1) > len(s2):
        ## "Remove" case:
        return s2 in removal_combs
    elif len(s1) < len(s2):
        ## "Insert" case:
        return isInserted(s1, s2)


