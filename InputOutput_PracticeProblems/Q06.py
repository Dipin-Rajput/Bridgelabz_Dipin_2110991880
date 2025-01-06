# 6) Write all content of a given file into a new file by skipping line number 5: Write a program to copy the content of a file into a new file, skipping the 5th line.

# Writing 10 lines in org.txt

with open("org.txt", "w") as f:
    f.write("Hello, world! \nPython is fun. \nData is powerful. \nAI is the future. \nKeep learning daily. \nSimple is better. \nCoding sparks ideas. \nBugs teach patience. \nDebugging is essential. \nEnd of file.")

# Reading original file

with open("org.txt", "r") as f:
    content = f.read()
    print(f"Content from original file:\n\n{content}")
print()

# Reading and Creating copy file for the content

with open("org.txt", "r") as source, open("copy.txt", "w") as destination:
    line_number = 0
    for line in source:
        line_number += 1
        if(line_number == 5):
            continue
        destination.write(line)

# Reading Copied file

with open("copy.txt", "r") as f:
    content = f.read()
    print(f"Content form copied file:\n\n{content}")
        

