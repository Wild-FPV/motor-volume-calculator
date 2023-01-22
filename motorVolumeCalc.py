import tkinter as tk
pi = 3.14159265359

vol = None

def calcVolume():
    
    Mwidth = width.get()
    Mheight = height.get()

    try:

        vol = pi*(float(Mwidth)/2)**2
    
        vol = vol*(float(Mheight))

    except:
        
        vol = 0
    
    vol = round(vol,2)
    print(vol)
    volResult.config(text = vol)

window = tk.Tk()
window.title("Motor volume calculator")

title = tk.Label(

    text="Motor stator volume calculator",
    fg="blue",
    width=80,
    height=4
)

title.pack(fill=tk.X)

widthLabel = tk.Label(text="Motor width")
width = tk.Entry(
    
    fg="black",
    bg="white",
    width=30
    
)

widthLabel.pack()
width.pack()

heightLabel = tk.Label(text="Motor height")
height = tk.Entry(
    
    fg="black",
    bg="white",
    width=30
    
)

heightLabel.pack()
height.pack()

calcButton = tk.Button(
    window,
    text="Calculate!",
    width=30,
    height=2,
    bg="white",
    fg="red",
    command = calcVolume
)

topButtonSpace = tk.Label(width=30,height=2)
topButtonSpace.pack()

calcButton.pack()

bottomButtonSpace = tk.Label(width=30,height=2)
bottomButtonSpace.pack()

volumeLabel = tk.Label(text="Volume : ")
volResult = tk.Label(text = vol,bg="#F0A0A0",height=4)


volumeLabel.pack()
volResult.pack(fill=tk.X)

window.mainloop()