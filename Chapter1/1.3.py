## Chapter 1 - 1.3) URLify

## Use this to make sure that your list doesn't contain "" elements. It messes the output!
def remove_space_from_list(input_list):
    new_list = []
    for element in input_list:
        if element != "":
            new_list.append(element)
    return new_list

## Main function
def urlify(string):
    my_list = string.split(" ")
    my_list = remove_space_from_list(my_list)
    print my_list
    output_string = ""
    for i in range(len(my_list)):
        output_string += my_list[i]
        if i < (len(my_list) - 1):
            output_string += "%20"
    return output_string

my_string = "Mr John Smith"
print urlify(my_string)

