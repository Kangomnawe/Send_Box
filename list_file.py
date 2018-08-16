import os
print("The files and the folders in {} are:".find(os.getcwd()))
items = os.listdir('.')
for item in items:
    print(item)
    