from pypdf import PdfReader,PdfWriter
import math
FILE = "G:\\My Drive\\Projects\\Python codes\\pdf2book\\tes45.pdf"
NEWFILE = "G:\\My Drive\\Projects\\Python codes\\pdf2book\\book.pdf"
writer = PdfWriter()
reader = PdfReader(FILE)

booklet_size = 40
num_of_booklets = math.ceil(len(reader.pages)/booklet_size)

for num in range(num_of_booklets):
    pages = reader.pages[num*booklet_size:(num+1)*booklet_size]
    pages_len = len(pages)
    # exstend the file pages
    printed_pages = math.ceil(pages_len/4)

    booklet_len = pages_len
    if booklet_len%4 != 0:
        booklet_len += 4-booklet_len%4
    for i in range(printed_pages):
        print(i)
        writer.add_page(pages[i*2+1])

        if((booklet_len - ((i+1)*2))>=pages_len):
            writer.add_blank_page(595.296,841.896)
        else:writer.add_page(pages[booklet_len - ((i+1)*2)])

        if((booklet_len - ((i+1)*2-1))>=pages_len):
            writer.add_blank_page(595.296,841.896)
        else:writer.add_page(pages[booklet_len - ((i+1)*2-1)])

        writer.add_page(pages[i*2])


writer.write(NEWFILE)