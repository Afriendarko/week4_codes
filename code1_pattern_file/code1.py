def search(fname , st):
    l_no = 0
    l = []
    with open(fname, "r") as file:
        for i in file:
            l_no +=1
            if st in i:
                l.append((l_no, i.rstrip()))
    return l

fname = input("Enter file name: ")
st = input("Enter pattern to search: ")
search(fname ,st)