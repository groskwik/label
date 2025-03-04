# Label Printing Script with Delay to Prevent Printer Jams

This Python script facilitates the printing of PDF labels, introducing a delay between printing each page to mitigate the risk of printer jams, which are common when handling label stickers.

## Features

- **Printer Selection**: Allows users to choose from a predefined list of printers.
- **Sequential Page Printing with Delay**: Prints each page of a PDF individually, incorporating a user-defined delay between pages to prevent printer jams.

## Requirements

- **Operating System**: Windows
- **Python Libraries**:
  - `pywin32`
  - `PyMuPDF`

## Installation

1. **Install Python**: Ensure Python 3.x is installed on your system. Download it from the [official Python website](https://www.python.org/).

2. **Install Required Libraries**:
   - `pywin32`:
     ```bash
     pip install pywin32
     ```
   - `PyMuPDF`:
     ```bash
     pip install pymupdf
     ```

## Usage

1. **Prepare the Script**: Save the provided script to a `.py` file.

2. **Define the PDF to Print**: Specify the path to your PDF file in the script:
   ```python
   pdf_path = r"label.pdf"  # Replace with your actual file path
   ```


3. **Run the Script**: Execute the script using a terminal or command prompt:
   ```bash
   python script_name.py
   ```


4. **Select Printer**: When prompted, enter the number corresponding to the desired printer from the list provided.

5. **Printing Process**: The script will print each page of the specified PDF individually, introducing a delay (default is 20 seconds) between pages to prevent printer jams.

## Functions

- `select_printer()`: Prompts the user to select a printer from the predefined list.

- `print_pdf_with_delay(pdf_path, printer_name, delay=20)`: Prints each page of the specified PDF individually, with a delay between pages to prevent printer jams.

## Notes

- **Delay Adjustment**: The default delay between printing each page is set to 20 seconds. This can be adjusted by modifying the `delay` parameter in the `print_pdf_with_delay` function call:
  ```python
  print_pdf_with_delay(pdf_path, selected_printer, delay=20)  # Adjust delay as needed
  ```


- **Temporary Files**: The script creates temporary PDF files for each page to facilitate individual printing. These files are automatically deleted after printing.

- **Error Handling**: Ensure that the specified PDF file exists and that the printer is properly connected and configured. The script includes basic error handling to notify users of any issues during the printing process.

## License

This project is licensed under the MIT License.

## References

- [Simple Python Script for Label Printing - Ex Libris Developer Network](https://developers.exlibrisgroup.com/blog/simple-python-script-for-label-printing/)
- [Print PDFs automatically with python - Stack Overflow](https://stackoverflow.com/questions/72871943/print-pdfs-automatically-with-python)
- [Printer jams when trying to print PDF documents - Adobe Community](https://community.adobe.com/t5/acrobat-reader-discussions/printer-jams-when-trying-to-print-pdf-documents/td-p/9007424)

For further information on automating label printing with Python, consider exploring the [Simple Python Script for Label Printing](https://developers.exlibrisgroup.com/blog/simple-python-script-for-label-printing/) article. 
