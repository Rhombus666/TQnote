import datetime
print("Hi", input("What is your name? "))
while True:
    USRinput = input('command: ').strip()
    if USRinput == 'Qnote':
        print("Note saved:", input("Quick Note: "))
    elif USRinput == 'txt':
        TXT = input("Enter the content for your note: ")
        if TXT:
            filename = "notes_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt"
            with open(filename, "w") as file: 
                file.write(TXT + "\n"); print("New file created:", filename)
    elif USRinput.lower() == 'exit': 
        print("Goodbye!"); break
    else: 
        print("Unknown command. Try 'Qnote', 'txt', or 'exit'.")
