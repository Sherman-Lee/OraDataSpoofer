from appJar import gui
from spoofer import *
from ordered_set import OrderedSet
import os
import sys

class globe():
    headers = OrderedSet([])
    tick = 0
    items = ""

def press(button):
    if button == "Add Field":
        fName = app.getEntry("FieldName")
        fType = app.getRadioButton("FieldType")
        min = int(app.getEntry("Min (Must be >= 0)"))
        max = int(app.getEntry("Max"))
        globe.items = app.getTextArea("TxtArea")
        globe.headers.add((fName, min, max, fType))
        idlabel = "id" + str(globe.tick)
        globe.tick += 1
        app.addLabel(idlabel, fName + ", " + str(min) + ", " + str(max) + ", " + fType)
    elif button == "Clear All":
        globe.headers.clear()
    elif button == "Next":
        print(globe.items)
        gen(list(globe.headers), int(app.getEntry("Number of Records")), globe.items)

app = gui("Login Window", "1000x500")
app.addLabel("title", "Welcome to OraDataSpoofer", 0, 0, 3)
app.setLabelBg("title", "red")
app.setLabelFont("title", 20)
app.setFastStop(True)

app.startFrame("Left", row=1, column=0)
app.addLabelEntry("FieldName")
app.addRadioButton("FieldType", "Strings")
app.addRadioButton("FieldType", "Floats")
app.addRadioButton("FieldType", "Ints")
app.addRadioButton("FieldType", "Dates")
app.addRadioButton("FieldType", "Emails")
app.addRadioButton("FieldType", "Zips")
app.stopFrame()

app.startFrame("Middle", row=1, column=1)
app.addLabelNumericEntry("Min (Must be >= 0)")
app.addLabelNumericEntry("Max")
app.stopFrame()

app.startFrame("Right", row=1, column=2)
app.addLabel("Dictionary (Enter one item per line below; number of items must exceed Max) : ")
app.addTextArea("TxtArea")
app.addLabelNumericEntry("Number of Records")
app.stopFrame()

app.addButtons(["Add Field", "Clear All", "Next"], press)
app.go()