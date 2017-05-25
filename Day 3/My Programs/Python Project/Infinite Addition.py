def addition(list2):
    y = 1

    for x in range(len(list2) - 1):
        list2[y] = list2[x] + list2[y]


        y += 1
    print list2[len(list2) - 1:]

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
            ""


    print list2
    addition(list2)



if __name__ == "__main__":
    main()