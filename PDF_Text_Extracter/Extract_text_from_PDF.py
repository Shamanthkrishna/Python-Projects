import PyPDF2

# Open the PDF file
pdf = open("D:/SKB/Courses/Python Projects/PDF_Text_Extracter/Sample.pdf", "rb")

# Create a PDF reader object
reader = PyPDF2.PdfReader(pdf)

# Get the first page of the PDF
page = reader.pages[0]

# Extract text from the page
print(page.extract_text())

# Close the PDF file
pdf.close()
