
def gcd_iterative(a, b):
    if a > b:
        range0 = a
    elif b > a:
        range0 = b
    else:
        return a
    for i in range(1, range0):
        if a % i == 0 and b % 1 == 0:
            output = i
    return output

"""
@param a first number to be computed
@param b second number to be computed
@return  gives the GCD of a and b

iterative method
"""



def gcd_recursive(a, b):

    """
@param a first number to be computed
@param b second number to be computed
@return  gives the GCD of a and b

recursive method
"""


def reverse_str_iterative(str):
    out = ""
    for i in range(len(str) - 1, -1, -1):
        out += str[i]
    return out

"""
@param str   str to reverse
@return      reversed str

iterative method
"""


def reverse_str_recursive(str):

    """
@param str   str to reverse
@return      reversed str

recursive method
"""


def converter_iterative(a, b):
    output = ""
    while b != 0:
        quotient = b // a
        remainder = b % a
        output += str(remainder)
        b = quotient
    return output[::-1]

"""
@param a   the base to convert to
@param b   the number to be converted
@return    the converted answer

iterative method
"""


def converter_recursive(a, b):
    if b == 0:


"""
@param a   the base to convert to
@param b   the number to be converted
@return    the converted answer

iterative method
"""


def main():
    print gcd_iterative(40, 80)
    print gcd_recursive(40,80)
    print reverse_str_iterative("asdf")
    print reverse_str_recursive("asdf")
    print converter_iterative(8, 69)
    print converter_recursive(8, 69)


if __name__ == "__main__":
    main()