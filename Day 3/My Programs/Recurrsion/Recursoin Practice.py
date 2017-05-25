"""
PROGRAM
"""
"""
@ param x   the number that's digits are added
@ return    returns the sum of a number's digits

this is an iterative method for finding the sum of x's digits
"""


def sum_digits_iterative(x):
    total_sum = 0
    for index in range(len(str(x))):
        total_sum += (x % 10)
        x //= 10
    return total_sum

"""
@ param x   the number that's digits are added
@ return    returns the sum of a number's digits

this is an recursive method for finding the sum of x's digits
"""


def sum_digits_recursive(x):
    if x == 0:
        return 0
    else:
        return sum_digits_recursive(x // 10) + (x % 10)

"""
@param n number to convert
@return  returns binary conversion

iterative method
"""


def dec_to_bin_iterative(n):
    binary_string = ""
    while n != 0:
        quotient = n // 2
        remainder = n % 2
        binary_string += str(remainder)
        n = quotient
    return binary_string[::-1]

"""
@param n number to convert
@return  returns binary conversion

recursive method
"""


def dec_to_bin_recursive(n):
    if n == 0:
        return "0"
    else:
        return dec_to_bin_recursive(n // 2) + str(n % 2)

"""
@param str   the number you want to determine if it is a palindrome
@return      returns true or false whether str is a palindrome or not

an iterative method to find a palindrome
"""







def palindrome_iterative(str):
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



"""
@param str   the number you want to determine if it is a palindrome
@return      returns true or false whether str is a palindrome or not

recursive method to find a palindrome
"""


def palindrome_recursive(str):
    return True


def main():
    print palindrome_iterative("123321")
    print sum_digits_iterative(12345)
    print sum_digits_recursive(12345)
    print dec_to_bin_iterative(1000)
    print dec_to_bin_recursive(1000)


if __name__ == "__main__":
    main()