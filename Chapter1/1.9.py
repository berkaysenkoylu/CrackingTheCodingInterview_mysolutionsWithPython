## Chapter 1 - 1.9) String Rotation

## Obtain all possible rotations of the given string, s1
def rotate(inp, n=1):
    """This will rotate the given string by n times, it will output the rotated string!"""
    new_string = inp[n:] + inp[:n]
    return new_string

def rotations(inp):
    """This will return a list!"""
    rotation_list = []
    initial = inp
    for i in range(len(inp)):
        rotated = rotate(initial)
        rotation_list.append(rotated)
        initial = rotated
    return rotation_list


## Check if the s2 is included in the list that is obtained
def isSubstring(s1, s2):
    """This will return a bool: True or False!"""
    
    # Obtained all the rotations of s1
    rotation_list = rotations(s1)

    # Check if s2 is in the rotation list
    if s2 in rotation_list:
        return True
    else:
        return False


s1 = "waterbottle"
s2 = "erbottlewat"

print isSubstring(s1, s2)
