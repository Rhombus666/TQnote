Name = input("What is your name?")
print("Hi", Name)
while True:
    USRinput = input('command: ') #stuff
    
    if USRinput == 'Qnote': #more stuff
        NOTE1 = input("Quick Note: ")
        print(f"Note saved: {NOTE1}")
    
    elif USRinput == 'txt':
        NOTESAVE = input("Note: ")
        if NOTESAVE: 
            with open("notes.txt", "a") as file:
                file.write(NOTESAVE + "\n")
                print("Note saved")
    
    else:
        print("Unknown command")
