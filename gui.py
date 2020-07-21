import tkinter as tk
from tkinter import messagebox as tkinterMessage

import barcode

def generate_barcode():
    print("Generated Barcode")

print(barcode)

app = tk.Tk()

labelFrame = tk.LabelFrame(app, text="Barcode Sequence", padx=10, pady=10)
labelFrame.grid(row=0, column=0)

barcodeBeginningLabel = tk.Label(labelFrame, text="Barcode Sequence Beginning", padx=10, pady=20)
barcodeBeginningLabel.grid(row=1, column=0)

barcodeBeginningNumber = tk.IntVar()
barcodeBeginningNumberEntry = tk.Entry(
    labelFrame,
    textvariable=barcodeBeginningNumber
)
barcodeBeginningNumberEntry.grid(row=1, column=1, sticky=tk.W)

# barcode ending
barcodeBeginningLabel = tk.Label(labelFrame, text="Barcode Sequence Ending", padx=10, pady=20)
barcodeBeginningLabel.grid(row=1, column=2)

barcodeEndingNumber = tk.IntVar()
barcodeEndingNumberEntry = tk.Entry(
    labelFrame,
    textvariable=barcodeEndingNumber
)
barcodeEndingNumberEntry.grid(row=1, column=3, sticky=tk.W)

# suffix and prefix


labelFrameSuffixPrefix = tk.LabelFrame(app, text="Barcode Prefix & Suffix", width='800')
labelFrameSuffixPrefix.grid(row=3, column=0)

barcodePrefixlabel = tk.Label(labelFrameSuffixPrefix, text="Barcode Prefix", padx=10, pady=20)
barcodePrefixlabel.grid(row=4, column=0)

barcodePrefixVar = tk.StringVar()
barcodeFrefixEntry = tk.Entry(
    labelFrameSuffixPrefix,
    textvariable=barcodePrefixVar
)
barcodeFrefixEntry.grid(row=4, column=1, sticky=tk.W)

# barcode suffix
barcodeSuffixLabel = tk.Label(labelFrameSuffixPrefix, text="Barcode Suffix", padx=10, pady=20)
barcodeSuffixLabel.grid(row=4, column=2)

barcodeSuffixVar = tk.StringVar()
barcodeSuffixEntry = tk.Entry(
    labelFrameSuffixPrefix,
    textvariable=barcodeSuffixVar
)
barcodeSuffixEntry.grid(row=4, column=3, sticky=tk.W)

generateButton =tk.Button(text = "Generate" , command = generate_barcode, pady = 20)
generateButton.grid(row=6, column=0, padx = 10, pady = 10)
# app setup
app.title("Barcode Generator")
app.geometry("800x500")
app.mainloop()
