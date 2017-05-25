
def str_common_character_counter(str):
    list1 = []
    list2 = []
    for i in range(len(str)):
        a = -1
        for x in range(len(str)):
            if str[i] == str[x]:
                a += 1
        list1.append(a)
        list2.append(list1[i])
    print list2
    for y in range(len(list2)):
        for o in range(len(list2)):
            if list2[y] >= list2[o]:
                a += 1
            else:
                a = 0
        if a == len(list2):
            print str[y]







def main():
    str_common_character_counter("///::aaaabbbyyyyy")



if __name__ == "__main__":
    main()