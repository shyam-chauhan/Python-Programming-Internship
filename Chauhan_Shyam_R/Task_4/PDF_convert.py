from pdf2jpg import pdf2jpg
from pypdf import PdfReader 
import os



class Pdf_to_image:
    def __init__(self):
        self.output_path = os.getcwd() + '\pdf2jpg'


    def pdf_to_image(self,file_path):
        pdf2jpg.convert_pdf2jpg(file_path, self.output_path, pages="ALL")
        print("Done, all pages are converted check directory")


class Pdf_to_txt:

    def pdf_to_txt(self,file_path):
        reader = PdfReader(file_path) 
        with open('ocr.txt','w') as f:
            for i in range(1,len(reader.pages)):
                page = reader.pages[i] 
                text = page.extract_text()
                f.write(text)
        print("Done, data saved in ocr.txt file")

def main():
    choice = int(input("Enter your choice \n 1. Convert PDF to image \n 2. Convert PDF to txt \n 3. Exit \n Enter Number :"))
    pdf_path = input("Enter full path of the PDF file : ")
    if(choice == 1):
        o = Pdf_to_image()
        o.pdf_to_image(pdf_path)
    elif(choice == 2):
        o = Pdf_to_txt()
        o.pdf_to_txt(pdf_path)
    elif(choice == 3):
        exit(0)


if __name__ == '__main__':
    main()