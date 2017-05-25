`"""
PROGRAM
"""
"""
@ param x   the number that's digits are added
@ return    returns the sum of a number's digits

this is an iterative method for finding the sum of x's digits
"""


def sum_digits_iterative(x):
    for i in range(len(x) - 1):
        y = int(x[i])
    for n in range(len(x) - 1):
        y += int(x[n + 1])







def main():
    print sum_digits_iterative("145")



if __name__ == "__main__":