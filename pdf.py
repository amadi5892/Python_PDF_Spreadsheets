# PDF = Portable Document Format
import PyPDF2

f = open('Working_Business_Proposal.pdf','rb') # rb = read binary; since we aren't working with normal text file
pdf_reader = PyPDF2.PdfFileReader(f)
# print(pdf_reader.numPages)
# page_one = pdf_reader.getPage(0) # retireve first page
# page_one_text = page_one.extractText() # view text
# # print(page_one_text)
# f.close()

# Here we took the first page of a pdf file and created a new pdf file with that page
# first_page = pdf_reader.getPage(0)
# pdf_writer = PyPDF2.PdfFileWriter()
# pdf_writer.addPage(first_page)
# pdf_output = open('some_brandNew_doc.pdf','wb')
# pdf_writer.write(pdf_output)
# f.close()
# pdf_output.close()

pdf_text = []

for num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(num)

    pdf_text.append(page.extractText())

f.close()
print(pdf_text)