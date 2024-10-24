import datetime
ERRORCOUNT = 0
USRname = input("What is your name?")
print("Hi",)
while True:
    USRinput = input('command: ')
    if USRinput == 'Qnote':
        print("Note saved:", input("Quick Note: "))
    elif USRinput == 'txt':
        TXT = input("Enter the content for your note: ")
            filename = "notes_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt"
            with open(filename, "w") as file: 
                file.write(TXT + "\n"); print("New file created:", filename)
    elif USRinput.lower() == 'exit': 
        print("Goodbye!"); break
    else: 
        ERRORCOUNT = ERRORCOUNT + 1 
        print("Unknown command Error number:", ERRORCOUNT)
        ERRORCOUNT = ERRORCOUNT + 1 
        
