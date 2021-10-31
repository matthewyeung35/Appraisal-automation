from PyPDF2 import PdfFileReader
def fill_pdf():
    pdf = PdfFileReader("import.pdf") 
    print(pdf.getNumPages())
    print(pdf.documentInfo)
    for page in pdf.pages:
        print(page.extractText())


    return

def main():
    fill_pdf()


if __name__ == "__main__":
    main()
