from guizero import App, Text, PushButton, Window, TextBox, ButtonGroup
# Interface for first screen

def exitmachine():
    mainpage.destroy()

mainpage = App("Bank of India ATM", width=600, height=600)
mainpage.bg = 246, 185, 72
txt1 = Text(mainpage, "Welcome to Bank of India ATM", size=32, font="Open sans", align="top")
txt2 = Text(mainpage, "\n\n\nPlease enter card to begin transaction\n\n\n", size=20)
txt3 = Text(mainpage, "Blind mode on", align="bottom", size=10)
exitm = PushButton(mainpage, command=exitmachine, text="Stop Machine", align="bottom")

def card_detected():

    mainpage.hide()
    pinpage.show()

# after command is used to automatically call a command after a specified time
mainpage.after(3000, card_detected)

# Second screen interface
pinpage = Window(mainpage, title="ATM pin screen", width=600, height=600, visible=False)
pinpage.bg = 246, 185, 72
txt4 = Text(pinpage, "Please enter your ATM pin:", size=20)
txt5 = Text(pinpage, "Blind mode on", align="bottom", size=10)
textbox1 = TextBox(pinpage, text="",hide_text=True)


# Gui for snooping alert
def startprog():
    mainpage.after(3000, card_detected)
    mainpage.show()


snooping = True
def check_camera():
    if pinpage.enabled:
        if snooping:
            if pinpage.yesno(title="Snooping alert", text="Someone is snooping ! Do you want to continue?"):
                pass
            else:
                pinpage.destroy()
                startprog()

# Function for checking the ATM pin
def check_pin():
    # To be checked using the database
    if textbox1.value == "1234":
        pinpage.destroy()
        optionpage.show()
    else:
        pinpage.info("Incorrect pin", "Please enter correct pin")
        textbox1.clear()

pinpage.after(6000, check_camera)
push1 = PushButton(pinpage, command=check_pin, text="Enter")

# Selected transaction
def selected_option():
    if choice.value == "1.Cash Withdrawal":
        optionpage.destroy()
        op1.show()
    elif choice.value == "2.Cash Deposit":
        optionpage.destroy()
        op2.show()
    elif choice.value == "3.Change PIN":
        optionpage.destroy()
        op3.show()
    elif choice.value == "4.Balance Enquiry":
        optionpage.destroy()
        op4.show()

# Options page interface
optionpage = Window(mainpage, title="ATM options", width=600, height=600, visible=False)
optionpage.bg = 246, 185, 72
txt6 = Text(optionpage, "Choose from the following options:", size=24)
txt7 = Text(optionpage, "Blind mode on", align="bottom", size=10)
choice = ButtonGroup(optionpage, options=["1.Cash Withdrawal", "2.Cash Deposit", "3.Change PIN", "4.Balance Enquiry"])
choice.text_size = 24
choice.text_color = "black"
push2 = PushButton(optionpage, command=selected_option, text="continue")

# UI for exit button
def exitall(a):

    if a == "1":
        op1.destroy()
        mainpage.show()

    elif a == "2":
        op2.destroy()
        mainpage.show()

    elif a == "3":
        op3.destroy()
        mainpage.show()

    elif a == "4":
        op4.destroy()
        mainpage.show()

# UI for confirm button after entering details for transaction
def confirm(x):

    if x == "1":
        op1.info("transaction successful", "Please collect money from dispenser")
        op1.hide()
        startprog()

    elif x == "2":
        op2.info("transaction successful", "Your money is deposited")
        op2.hide()
        startprog()

    elif x == "3":
        op3.info("transaction successful", "Your PIN is changed")
        op3.hide()
        startprog()

    elif x == "4":
        op4.info("transaction successful", "Please collect enquiry receipt")
        op4.hide()
        startprog()

# UI for option 1
op1 = Window(mainpage, "Cash Withdrawal", width=600, height=600, bg=(246, 185, 72), visible=False)
txt12 = Text(op1, "Please enter the amount to be withdrawn", size=20)
textbox2 = TextBox(op1)
confirm1 = PushButton(op1, text="Confirm", command=confirm, args="1")
txt8 = Text(op1, "Blind mode on", align="bottom", size=10)
exitbutton1 = PushButton(op1, text="Cancel transaction", command=exitall, args="1", align="bottom")


# UI for option 2
op2 = Window(mainpage, "Cash Deposit", width=600, height=600, bg=(246, 185, 72), visible=False)
txt13 = Text(op2, "Enter keep the cash in deposit machine", size=20)
txt14 = Text(op2, "The amount to be deposited is:10000", size=20)
confirm2 = PushButton(op2, text="Confirm", command=confirm, args="2")
txt9 = Text(op2, "Blind mode on", align="bottom", size=10)
exitbutton2 = PushButton(op2, text="Cancel transaction", command=exitall, args="2", align="bottom")



# UI for option 3
op3 = Window(mainpage, "Change PIN", width=600, height=600, bg=(246, 185, 72), visible=False)
txt15 = Text(op3, "Enter the current PIN", size=20 )
textbox3 = TextBox(op3,hide_text=True)
txt16 = Text(op3, "Enter the new PIN", size=20)
textbox4 = TextBox(op3,hide_text=True)
confirm3 = PushButton(op3, text="Confirm", command=confirm, args="3")
txt10 = Text(op3, "Blind mode on", align="bottom", size=10)
exitbutton3 = PushButton(op3, text="Cancel transaction", command=exitall, args="3", align="bottom")



# UI for option 4
op4 = Window(mainpage, "Balance enquiry", width=600, height=600, bg=(246, 185, 72), visible=False)
txt17 = Text(op4, "The balance is :10000", size=20)
confirm4 = PushButton(op4, text="Confirm", command=confirm, args="4")
txt11 = Text(op4, "Blind mode on", align="bottom", size=10)
exitbutton4 = PushButton(op4, text="Cancel transaction", command=exitall, args="4", align="bottom")

# Start for program
mainpage.display()
