import datetime
print ("Welcome to textnote")
print ("The text based, Python based note taking software for Windows")
USRname = input("What is your name? ")  # Asks what your name is
print("Hi", USRname)  # shows hi

while True:
    USRinput = input('Command: ')
    if USRinput == 'Qnote':
        Qnote = input("Quick Note: ")
        print(Qnote)
    elif USRinput == 'txt':
        TXT = input("TXT note: ")
        filename = "notes_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt"
        with open(filename, "w") as file: 
            file.write(TXT + "\n")
        print("New file created:", filename)
    elif USRinput.lower() == 'exit':
        print("Goodbye!")
        break  # shows goodbye
    else:
        print("Unknown command")
