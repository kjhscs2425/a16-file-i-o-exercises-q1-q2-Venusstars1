# Read "romeo_and_juliet.txt" (The full text of Shakespeare's Romeo and Juliet)

with open("romeo_and_juliet.txt", "r") as f:
    text = f.read()
    for line in f:
        if "Juliet" in line:
            total += 1
print(total)

# Count how many times the word "Juliet" appears
