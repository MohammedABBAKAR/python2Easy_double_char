# Given a string, you have to return a string in which each character 
# (case-sensitive) is repeated once.

# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "





# def double_char(s):
#     return ''.join([char * 2 for char in s])


def double_char(s):
    result = ''
    for char in s:
        result += char * 2
    return result


print(double_char("String"))  