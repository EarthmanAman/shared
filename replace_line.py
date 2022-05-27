file_name = input("Enter a filename: ")
old_string = input("Enter the old string to be replaced: ")
new_string = input("Enter the new string to replace the old string: ")

try:
    doc = []
    with open(file_name, "r") as file:
        lines = file.readlines()
        for line in lines:
            words = line.split()
            idx = words.index(old_string)
            print(idx)
            if type(idx) == int:
                words[idx] = new_string
            print(words)
            doc.append(words)

    with open(file_name, "w") as file:
        doc_string = ""
        for line in doc:
            for word in line:
                doc_string += word
                doc_string += " "
            doc_string += "\n"
        file.write(doc_string)
except:
    print("Error: Could not opened the file.")
