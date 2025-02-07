def reverse():
    fi = open("input.dat", mode="rb")
    fo = open("output.dat", mode="wb")
    fo.write(fi.read()[::-1])
    fi.close()
    fo.close()

reverse()