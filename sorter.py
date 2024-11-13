import sys
import os
import shutil

userInput = input("Sort all files into folders based on extension type in the current directory.\nEnter to continue or [x] to cancel.\n")
if userInput.lower() == "x":
    sys.exit()
directory = sys.path[0]
fileList = (os.listdir(directory))

for file in fileList:
    if file != os.path.basename(__file__):
        try:
            index = file.rindex(".")
            ext = file[index+1:]
            if not os.path.exists(directory+r"\\" + ext+ " Files"):
                os.makedirs(directory+r"\\" + ext+ " Files")
            shutil.move(directory+r"\\"+file, directory+r"\\" + ext+ " Files")
        except ValueError:
            pass
