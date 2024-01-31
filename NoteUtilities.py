import random as rand

noteList = ["test1", "test2", "test3", "test4"]
lastNote = 4

def addNote():
    global lastNote, noteList
    newNote = input("What would you like to add to the note?")
    noteList.append(newNote)
    lastNote += 1

def displayNotes():
    global noteList
    for note in range(0, lastNote):
        print(str(note + 1) + ". " + noteList[note] + "\n")

def displayRandomNote():
    global noteList, lastNote
    randNote = rand.randint(0, lastNote)

    print(noteList[randNote] + "\n")

def addAndDisplay():
    addNote()
    displayNotes()

def removeLastNote():
    global noteList, lastNote
    noteList[lastNote-1] = ""
    lastNote -= 1

def deleteNote(numNote):
    global noteList, lastNote

    if numNote < 0 or numNote > lastNote:
        print("Sorry, but you made an invalid selection.")
        print("Please try again.")

    elif numNote == lastNote:
        removeLastNote()
    else:
        for index in range(numNote-1, lastNote-1):
            noteList[index] = noteList[index + 1]
        removeLastNote()
        print("Note deleted.")
