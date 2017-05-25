def sort(list2):
    z = 0
    a = 1
    b = 0
    for u in range(len(list2) - 1):
        for i in range(len(list2) - 1):
            map(int, list2)
            if list2[z] > list2[a]:
                b = list2[a]
                list2[a] = list2[z]
                list2[z] = b
            z += 1
            a += 1
        z = 0
        a = 1
    print list2

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
    sort(list2)




if __name__ == "__main__":
    main()