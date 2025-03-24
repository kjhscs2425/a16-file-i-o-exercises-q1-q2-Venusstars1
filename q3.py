# Read "romeo_and_juliet.txt" (The full text of Shakespeare's Romeo and Juliet)

with open("romeo_and_juliet.txt", "r") as f:
    text = f.read()

with open("romeo_and_juliet.txt", "r") as f:
    total = 0
    for line in f:
        if "Juliet" in line:
            total += 1
        else:
            pass
print(total)

# Count how many times the word "Juliet" appears
