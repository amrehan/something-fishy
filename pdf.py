import PyPDF2

pdfFileObj = open('example.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

print(pdfReader.numPages)


my_text = ''
for i in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(i)
    my_text += pageObj.extractText()

encoded = ''
my_text = my_text.upper()

for i in my_text:
    if i == 'A':
        encoded += '4'
    elif i == 'T':
        encoded += '7'
    elif i == 'E':
        encoded += '3'
    elif i == 'I':
        encoded += '1'
    elif i == 'L':
        encoded += '1'
    elif i == 'z':
        encoded += '2'
    elif i == 'Q':
        encoded += 'O'
    elif i == 'L':
        encoded += 'M'
    elif i == 'M':
        encoded += '|-|'
    else:
        encoded += str(ord(i))
pdfFileObj.close()

# you can do it the way you like it

# after all "INT3LL1G3NC3 1S 7H3 4B1L17Y 70 4DAP7 TO CHANG35 "
