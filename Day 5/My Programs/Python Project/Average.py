def average(list2):
    a = list2[0]
    for x in range(1, len(list2)):
        a = list2[x] + a
    print a/len(list2)



def main():
    while True:
        try:
            list2 = []
            current_entry = int(raw_input("Please enter a number"))
            while current_entry != -99999:
                list2.append(current_entry)
                current_entry = int(raw_input("Please enter a number"))
            break
        except ValueError:
            "Please enter a integer"
    print list2
    average(list2)


if __name__ == "__main__":
    main()