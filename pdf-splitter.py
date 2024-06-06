import argparse
from PyPDF2 import PdfReader, PdfWriter

#Usage
#python pdf-splitter.py input.pdf 1 5 output.pdf

def split_pdf(input_file, start_page, end_page, output_file):
    reader = PdfReader(input_file)
    writer = PdfWriter()
    page_range = range(start_page, end_page + 1)
    for page_num, page in enumerate(reader.pages, 1):
        if page_num in page_range:
            writer.add_page(page)
    with open(output_file, 'wb') as out:
        writer.write(out)

def main():
    parser = argparse.ArgumentParser(description='PDF Splitter CLI')
    parser.add_argument('input_file', help='Path to the input PDF file')
    parser.add_argument('start_page', type=int, help='Start page number')
    parser.add_argument('end_page', type=int, help='End page number')
    parser.add_argument('output_file', help='Path to the output PDF file')
    args = parser.parse_args()

    split_pdf(args.input_file, args.start_page, args.end_page, args.output_file)
    print(f"PDF split successfully. Output saved as {args.output_file}")

if __name__ == '__main__':
    main()