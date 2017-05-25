

def sort_dictionary(dictionary):
    entry = 1
    y = 1
    output = {}
    output[1] = dictionary[1]
    for x in range(1, len(dictionary) + 1):
        while dictionary[x] > dictionary[y]:
            if dictionary[x] < dictionary[y]:
                entry *= 2
                output[entry] = dictionary[x]
                y += 1
            else:
                output[entry + 1] = dictionary[x]
    for random in range(1 ** len(dictionary)):
        output[random] = chr(output[random])

    return output

def main():
    x = 1
    bintree = {}
    num = int(raw_input("Enter the number of letters you want to enter."))
    for i in range(num):
        input = (raw_input("Please enter a letter."))
        a = ord(input)
        bintree[x] = a
        x += 1
    print bintree
    print sort_dictionary(bintree)




if __name__ == "__main__":
    main()