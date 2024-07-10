from PyPDF2 import PdfReader, PdfWriter

file_name = input("Enter the full path of the PDF file: ")
start_page = int(input("Enter the starting page number: "))
end_page = int(input("Enter the ending page number: "))

reader = PdfReader(file_name)
total_pages = len(reader.pages)
writer = PdfWriter()
page_range = range(start_page, end_page + 1)

if (end_page >  total_pages):
    print("End page value is greater than total pages !")

else:
    for page_num, page in enumerate(reader.pages, 1):
        if page_num in page_range:
            writer.add_page(page)

    output_file = f'{file_name}_page_{start_page}-{end_page}.pdf'
    with open(output_file, 'wb') as out:
        writer.write(out)

    print(f'Pages {start_page} to {end_page} extracted to {output_file}')
