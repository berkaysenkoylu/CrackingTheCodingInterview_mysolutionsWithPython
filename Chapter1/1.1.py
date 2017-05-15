## Chapter 1 - 1.1) Is Unique

def isUnique(string):
    return len(set(string)) == len(string)

## Alternative way, maybe?
def isUniqueTwo(string):
    newStr = ""
    for letter in string:
        if letter not in newStr:
            newStr += letter
    return newStr == string

## Alternative alternative way, maybe?
def isUniqueThree(string):
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
##                print string[i], string[j]
                return False
    return True
            

print isUnique("berkay")
print isUniqueTwo("berkay")
print isUniqueThree("berkay")
