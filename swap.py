def swapfile():
    file1 = input("enter your 1st file")
    file2 = input("enter your 2nd file")
    with open(file1,"r")as A:
        dataA= A.read()
    with open(file2,"r")as b:
        datab= b.read()
    with open (file1,"w")as A:
        A.write(datab)
    with open (file2,"w")as b:
        b.write(dataA)
swapfile()
        