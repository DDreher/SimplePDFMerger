# SimplePDFMerger
SimplePDFMerger is exactly what it says: A very simple script to merge PDFs using [PyPDF2](https://github.com/mstamy2/PyPDF2), without any bells and whistles.

## Usage
1. Create a new virtual environment
2. Install the requirements with `pip install -r requirements.txt`
3. Put the PDFs you want to merge into the `input` folder. PDFs will be merged in alphabetic order. Name your files accordingly, if you want to specify an order, e.g. `00_FirstPDF.pdf, 01_SecondPDF.pdf, 02_ThirdPDF.pdf, ...`
4. Run `python pdfmerger.py`
5. Your merged PDF will be in the `output` folder called `result.pdf`. If there already exists an output file, it will be overwritten.
