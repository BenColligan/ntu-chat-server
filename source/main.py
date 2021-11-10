# Title: NTU Chat Server
# Author: Benjamin Colligan
from tkinter import *        

# Functions

def updateLog():
    with open("servers/" + serverIDEntryBox.get() + ".txt", "a+") as log:
        log.write(usernameEntryBox.get() + ": " + messageEntryBox.get() + "\n")    

def updateChatBoxText():
    if serverIDEntryBox.get() != "":
        with open("servers/" + serverIDEntryBox.get() + ".txt", "r") as log:
            chatBoxText.set(log.read())
            # print("Chat updated")
    root.after(1000, updateChatBoxText)

def sendMessage():
    updateLog()
    updateChatBoxText()

# GUI preconfiguration

root = Tk()
root.title("NTU Chat Server - Local Machine Only")
root.geometry("900x900")
chatBoxText = StringVar()

# Making the GUI elements
        
# Config Panel Frame
configPanelFrame = Frame(root, bg = "#e069ab")
configPanelFrame.pack(fill=X)

# Username Entry Label
usernameEntryLabel = Label(configPanelFrame, text = "Username:", font = "Candara 12", bg = "#e069ab", fg = "white")
usernameEntryLabel.pack(side=LEFT, fill=X)

# Username Entry Box
usernameEntryBox = Entry(configPanelFrame)
usernameEntryBox.pack(side=LEFT, expand=TRUE, fill=X)

# Server ID Entry Label
serverIDEntryLabel = Label(configPanelFrame, text = "Server ID:", font = "Candara 12", bg="#e069ab", fg = "white")
serverIDEntryLabel.pack(side=LEFT, fill=X)

# Server ID Entry Box
serverIDEntryBox = Entry(configPanelFrame)
serverIDEntryBox.pack(side=LEFT, expand=TRUE, fill=X)

# Chat Box Label
chatBoxLabel = Label(root, textvariable = chatBoxText, bg = "pink", font = "Candara 16", anchor = NW, justify = LEFT)
chatBoxLabel.pack(expand = TRUE, fill = BOTH)

# Message Entry Frame
messageEntryFrame = Frame(root)
messageEntryFrame.pack(fill = BOTH, anchor = S)

# Message Entry Box
messageEntryBox = Entry(messageEntryFrame, font = "Candara 12")
messageEntryBox.pack(side = LEFT, fill = BOTH, expand = TRUE)

# Message Send Button
messageSendButton = Button(messageEntryFrame, text = "Send", command=sendMessage, font = "Candara 12", bg="#e069ab", fg = "white")
messageSendButton.pack(expand = TRUE)

root.after(1000, updateChatBoxText)

root.mainloop()










