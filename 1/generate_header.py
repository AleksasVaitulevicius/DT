file = open("header.txt", "a")
for it in range(0, 280):
        file.write("@ATTRIBUTE " + `it` + " NUMERIC\n")