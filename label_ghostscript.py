#!/usr/bin/env python
import time
import tempfile
import os
import subprocess

PRINTER_NAME = "Brother HL-L3290CDW [Wireless]"
# Path to Ghostscript executable
ghostscript_path = r"C:\Program Files\gs\gs10.04.0\bin\gswin64c.exe"  # Update if needed

def print_pdf(pdf_path, delay=20):
    """Prints each page of a PDF with a delay using Ghostscript."""
    try:

        printer_name = PRINTER_NAME
        print(f"Using printer: {printer_name}, printing: {printer_name}")
        # Use Ghostscript to print directly
        print(f"Printing {pdf_path}")
        
        gs_command = [
            ghostscript_path,
            "-sDEVICE=mswinpr2",  # Windows print device
            "-dNOPAUSE",
            "-dBATCH",
            f"-sOutputFile=%printer%{printer_name}",
            pdf_path
        ]

        # Run Ghostscript command
        subprocess.run(gs_command, check=True)
        
        print("Printing complete.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    pdf_path = "label.pdf"  # Replace with your actual PDF file path
    print_pdf(pdf_path)

