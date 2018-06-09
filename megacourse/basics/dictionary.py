def dict(word, file = "dict.txt"):
    print("Starting")
    try:
        fptr = open(file, "a+")
    except:
        print("Error opening the database file.")
        exit()

# Rewind the file to the beginning
# append mode fast-forwards to the end automatically
    fptr.seek(0)
    words = fptr.read()
    print(words)
    if word in words:
        print("Word", word, "is already in the dictionary")
    else:
        print("Adding", word, "to the dictionary.")
        fptr.writelines(word + "\n")
        fptr.write("\n")
    fptr.close()
