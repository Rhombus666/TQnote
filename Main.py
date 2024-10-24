import datetime

Name = input("What is your name? ")
print("Hi", Name)

while True:
    USRinput = input('command: ').strip()
    
    if USRinput == 'Qnote':
        Qnote = input("Quick Note: ")
        print(f"Note saved: {Qnote}")
    
    elif USRinput == 'txt':
        TXT = input("Enter the content for your note: ")
        if TXT:
            filename = "notes_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt"
            with open(filename, "w") as file:
                file.write(TXT + "\n")
            print(f"New file created: {filename}")
    else:
        print("Unknown command. Try 'Qnote', 'txt', or 'exit'.")
