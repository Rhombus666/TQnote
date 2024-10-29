import datetime

ERRORCOUNT = 0
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
        ERRORCOUNT += 1
        print("Unknown command. Error number:", ERRORCOUNT)
