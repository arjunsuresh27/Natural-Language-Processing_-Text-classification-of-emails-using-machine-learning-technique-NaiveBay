import os
name="nboutput.txt"
for root, dirs, files in os.walk("C:\\"):
    if name in files:
        print(os.path.join(root,name))