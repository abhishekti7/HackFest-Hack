def writeFile(string):
    with open('test.txt',"w") as f:
        f.write(string)
    f.close()