import tkinter as tk
from tkinter import messagebox as tkinterMessage
from tkinter import filedialog
import barcode
from barcode.writer import ImageWriter
from PIL import *

def check_errors():
    """
    Purpose: to check for errors in the input in the entry field

    Pre-Conditions:

    Post-Conditions:

    Return:
    :return: true or false
    """
    start = barcodeBeginningNumber.get()
    end = barcodeEndingNumber.get()

    if end < start:
        tkinterMessage.showerror("Input Error", "Please Input the Right Ending Sequence")
        return False
    else:
        return True

def generate_barcode():
    print("Generated Barcode")
    start = barcodeBeginningNumber.get()
    end = barcodeEndingNumber.get()
    prefix = barcodePrefixVar.get()
    suffix = barcodeSuffixVar.get()


    print("Start , End, Prefix, Suffix", start, end, prefix, suffix)

    if check_errors():
        try:
            save_in = filedialog.askdirectory()
        except:
            tkinterMessage.showerror("Wrong Directory", "Chose the Correct Directory")
            save_in = filedialog.askdirectory()
        print(save_in , type(save_in))
        # barcode.PROVIDED_BARCODES
        # [u'code39', u'code128', u'ean', u'ean13', u'ean8', u'gs1', u'gtin',
        #  u'isbn', u'isbn10', u'isbn13', u'issn', u'jan', u'pzn', u'upc', u'upca']

        # all the possible barcodes provided by the class
        # print(barcode.PROVIDED_BARCODES)
        # ['code128', 'code39', 'ean', 'ean13', 'ean14', 'ean8', 'gs1', 'gtin',
        #  'isbn', 'isbn10', 'isbn13', 'issn', 'itf', 'jan', 'pzn', 'upc', 'upca']

        if type(save_in) == str and save_in != ():
            CODE128 = barcode.get_barcode_class('code128')
            print('condition passed')
            for i in range(start, end + 1):

                codeFor = prefix +  str(i) + suffix
                try:
                    code128 = CODE128(codeFor, writer=ImageWriter())
                    fullname = code128.save(save_in + '/barcode' + str(i))
                    print(fullname)
                except PermissionError:
                    tkinterMessage.showerror("Permission Denied", "Not Enough Permission to Write the Files")
                    return


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
