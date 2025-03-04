#!/usr/bin/env python
import win32print
import os
import time
import fitz  # PyMuPDF for extracting pages
import tempfile

# Set your printer name
PRINTER_NAME = "Brother HL-L3290CDW [Wireless]"

def print_pdf_with_delay(pdf_path, delay=20):
    """Prints each page of a PDF separately with a delay using Win32 API."""
    try:
        # Open the printer
        printer_name = PRINTER_NAME
        print(f"Using printer: {printer_name}")

        # Open the PDF document
        doc = fitz.open(pdf_path)

        for page_num in range(len(doc)):
            # Create a temporary PDF file for the single page
            temp_pdf = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
            temp_path = temp_pdf.name
            temp_pdf.close()

            # Extract the single page into a new document
            new_doc = fitz.open()
            new_doc.insert_pdf(doc, from_page=page_num, to_page=page_num)
            new_doc.save(temp_path)
            new_doc.close()

            print(f"Printing page {page_num + 1}...")

            # Open printer
            hprinter = win32print.OpenPrinter(printer_name)
            win32print.StartDocPrinter(hprinter, 1, (f"Print Job - Page {page_num + 1}", None, "RAW"))
            win32print.StartPagePrinter(hprinter)

            # Read and send the file
            with open(temp_path, "rb") as f:
                win32print.WritePrinter(hprinter, f.read())

            win32print.EndPagePrinter(hprinter)
            win32print.EndDocPrinter(hprinter)
            win32print.ClosePrinter(hprinter)

            # Wait before printing the next page
            time.sleep(delay)

            # Delete the temporary file
            os.remove(temp_path)

        print("Printing complete.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    pdf_path = r"label.pdf"
    print_pdf_with_delay(pdf_path, delay=20)

