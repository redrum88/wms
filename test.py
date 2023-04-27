import os
# Walk through current directory and print all files and directories
path = os.getcwd()
for root, dirs, files in os.walk(path):
    for file in files:
        print(file)
    for dir in dirs:
        print(dir)