ff = open("wiki.txt", "r")

numberoflines = 0
numberofwords = 0
numberofcharacters = 0
for line in ff:
  line = line.strip("\n")

  words = line.split()  
  numberoflines += 1
  numberofwords += len(words)
  numberofcharacters += len(line)

ff.close()

print("lines:", numberoflines, "words:", numberofwords, "characters:", numberofcharacters)
