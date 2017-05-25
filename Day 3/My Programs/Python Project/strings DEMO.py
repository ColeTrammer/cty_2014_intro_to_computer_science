"""
String_Demo.py

In this program, we're going to demonstrate the capabilities of the String data type in python.

Q: What is a string?
A: A str is a set of characters grouped together.

Q: How do we distinguish a str from any other  data type.
A:Strings are determined by quotation marks.

"""
"""
@param str   The string to have every character printed

Prints every character of the string sre
on a seperate line
"""
def line_by_line(str):

    for i in range(len(str)):
        print str[i]

"""
@ param str   The string to have every other character printed

Prints every other character of the string str
on a seperate line starting at index 0
"""

def line_by_line_skip(str):
    i = 0
    while i <= len(str) - 1:
        print str[i]
        i += 2

"""
@ param str A string to be printed backward

Prints every character of the String str
starting at the last character
going backwards
ending at the 0th character
"""

def line_by_line_backward(str):
    for i in range(len(str) - 1, -1, -1):
        print str[i]

"""
@param str  The string whose vowels we 're counting

Counts the number of vowels in str
And returns the value
"""

def count_vowels(str):
    a = 0
    for i in range(0, len(str)):
        if str[i] == "a" or str[i] == "e" or str[i] == "i" or str[i] == "o" or str[i] == "u":
            a += 1
    print a

"""
@param sre  Is str a palindrome

Returns True if str is a palindrome
Returns False if str is not a palindrome
"""

def is_palindrome(str):
    a = 1
    for i in range(len(str)):
        if str[i] == str[len(str) - a]:
            b = 0
            a += 1
        elif str[i] != str[len(str) - a]:
            b = 1
            a += 1
            return False
    if b == 0:
        return True







def main():
    #declare a string
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    #len(STRINGNAME) returns the number of characters
    #                in STRINGNAME

    #Accessing a particular index
    #
    #  STRINGNAME[INDEX_VALUE]
    #
    print alphabet[0]
    print alphabet[4]
    print alphabet[25]
    print alphabet[len(alphabet) - 1]

    #Splicing
    #To splice a String from index A to Index B
    #
    #STRINGNAME[A:B + 1]
    #
    print alphabet[0:5]
    print alphabet[:5]

    line_by_line(alphabet)

    line_by_line_skip(alphabet)

    line_by_line_backward(alphabet)

    count_vowels(alphabet)

    print is_palindrome("")




if __name__ == "__main__":
    main()