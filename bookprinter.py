import sys
import math
from pypdf import PdfReader, PdfWriter, PaperSize


### input 
try:

    filename = sys.argv[1]
    file = PdfReader(filename)

    numPages = len(file.pages)

except:

    print('could\'nt open file')
    exit()


numSheets = math.ceil(numPages / 4)
numTotal = numSheets * 4

order = [None] * (numTotal)

### preenchimento em pares
ii = 0

# etapa A: frente
cc = 0

while cc < (numTotal / 2):
    order[ii + 0] = numTotal - cc
    order[ii + 1] = 1 + cc

    ii += 2
    cc += 2

# etapa B: verso
cc = 0

while cc < (numTotal / 2):
    order[ii + 0] = 2 + cc
    order[ii + 1] = numTotal - (cc + 1)

    ii += 2
    cc += 2

# print(order)

### monta o novo pdf

try: 

    newfile = PdfWriter()

    # insere as paginas no novo pdf
    for jj in order:
        # paginas do arquivo original
        if jj <= numPages: 
            newfile.add_page(file.pages[jj - 1])
        # blanks
        else:
            newfile.add_blank_page(PaperSize.A4.width, PaperSize.A4.height)

    newfile.write(filename.replace('.pdf', '') + '_reordered.pdf')

except:

    print('could\'nt create new file')
    exit()

print("Printer will use " + str(numSheets) + " sheets")
print("Keep in mind that each sheet will be printend on the front and back")
print("Remember to place the sheets in the correct order and oridentation")