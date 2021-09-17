import os
if os.path.exists("test.txt"):
    os.remove("test.txt")
    # os.rmdir("folder name")
else:
    print("file not found")