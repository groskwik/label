
import fitz  # PyMuPDF for PDF reading
import time
import tempfile
import win32print
import win32api
import os

def print_pdf_with_delay(pdf_path, delay=20):
    """Prints each page of a PDF with a delay using Windows printing API."""
    try:
        doc = fitz.open(pdf_path)
        printer_name = win32print.GetDefaultPrinter()  # Get default printer

        for page_num in range(len(doc)):
            # Create a temporary PDF file with a single page
            temp_pdf = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
            temp_path = temp_pdf.name
            temp_pdf.close()

            new_doc = fitz.open()  # Create a new empty PDF
            new_doc.insert_pdf(doc, from_page=page_num, to_page=page_num)
            new_doc.save(temp_path)
            new_doc.close()

            # Print the temporary PDF file
            print(f"Printing page {page_num + 1}...")
            win32api.ShellExecute(0, "print", temp_path, f'/d:"{printer_name}"', ".", 0)

            # Wait before printing the next page
            time.sleep(delay)

            # Delete the temporary file
            os.remove(temp_path)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    pdf_path = "label.pdf"  # Replace with your PDF file path
    print_pdf_with_delay(pdf_path)
