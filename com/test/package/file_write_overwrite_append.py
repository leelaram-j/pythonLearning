try:
    f = open("test.txt", "a") # use w for overwrite, a for append mode
    f.write("\nIm learning python")
    f.close()

    f = open("test.txt", "r")
    print(f.read())
except Exception as e:
    print(e)
else:
    f.close()