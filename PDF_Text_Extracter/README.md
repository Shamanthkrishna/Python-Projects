# PDF Text Extractor

A simple Python project to extract text from PDF files using the PyPDF2 library.

## Requirements

- Python 3.x
- PyPDF2 library

## Installation

1. Clone this repository or download the source code.
2. Install the PyPDF2 library using pip:
   ```sh
   pip install PyPDF2
   
## Usage
1. Place your PDF file in the project directory.
2. Update the file path in the script to point to your PDF file.
3. Run the script to extract and print text from the first page of the PDF.

## Code
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
