## Chapter 1 - 1.6) String Compression


def compressor(string):
    pointer = 0
    mylist = []
    final = ""
    while(pointer < len(string)):
        for j in range(pointer + 1, len(string)):
            if string[pointer] != string[j]:
                mylist.append(string[pointer:j])
                pointer = j
                break
            if j == len(string) - 1:
                mylist.append(string[pointer:])
                pointer = len(string)
                break

    for i in mylist:
        final += i[0] + str(len(i))
        
    if len(final) == len(string):
        return string
    else:
        return final



print compressor("aabcccccaaacccggggtttt")
            
        
