n = int(input("how many characters to priview?"))
file = open("classnotes.txt", "r")
print(file.read(n))
file.close()
print()

file = open("classnotes.txt", "r")
lines = file.readlines()
file.close()
print("Total lines:", len(lines))
for i in range(len(lines)):
    print(i + 1, "->", lines[i].strip())
print()

word = input("Skip lines starting with:")
file = open("classnotes.txt", "r")
for line in file:
    if line.startswith(word):
        print("Skip ->", line.strip())
    else:
        print("Keep ->", line.strip())
file.close()
print()

file = open("classnotes.txt", "r")
lines = file.readlines()
file.close()
out = open("odd-lines.txt", "w")
for i in range(0, len(lines), 2):
    out.write(lines[i])
out.close
print("odd lines saved to odd-lines.txt")
