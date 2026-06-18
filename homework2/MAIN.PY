import os

print("===  Art Notes ===")
with open("art-notes.txt", "r") as f:
    for line in f:
        print(line.strip())
print()

print("===  Work Notes ===")
with open("english-notes.txt", "r") as f:
    for line in f:
        words = line.split()
        print(len(words), "words ->", line.strip())
print()

print("=== Merging Notes===")
if os.path.exists("all-notes.txt"):
    print("all-notes.txt already exists, overwriting")
else:
    print("all-notes.txt not found, creating")

content = ""
with open("art-notes.txt", "r") as f:
    content += "--- art-notes.txt ---\n"
    content += f.read() + "\n"
with open("english-notes.txt", "r") as f:
    content += "--- english-notes.txt ---\n"
    content += f.read() + "\n"
with open ("all-notes.txt", "w") as out:
    out.write(content)
print("saved to all-notes.txt")#
print()

if os.path.exists("all-notes.txt"):
    os.remove("all-notes.txt")
    print("all-notes.txt removed")
else:
    print("all-notes.txt does not exist")
