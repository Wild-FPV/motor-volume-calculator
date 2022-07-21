from math import pi
import pyperclip as pc

while True:

    print("\n")
    width = input("Motor stator width : ")
    height = input("Motor stator height : ")

    width = float(width)
    height = float(height)

    vol = pi*(width/2)**2
    vol = vol*(height)

    print("Stator volume is : " + str(vol))
    pc.copy(round(vol,2))
