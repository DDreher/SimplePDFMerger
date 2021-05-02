import os

from PyPDF2 import PdfFileMerger

INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"
OUTPUT_NAME = "result.pdf"
PDF_EXTENSION = ".pdf"


def get_pdf_in_folder(path):
    """
    Returns a sorted list of paths for pdf files contained in the given path

    :param path: The path to check for pdf files
    :return: A sorted list of paths to pdf files in the given folder
    """
    pdf_paths = [os.path.join(path, f) for f in os.listdir(path) if f.endswith(PDF_EXTENSION)]
    return sorted(pdf_paths)


if __name__ == "__main__":
    """
    Merge pdf files contained in './input/' and write the merged result to './output/'.
    File are merged in alphabetic order.
    The easiest way to ensure a specific order is to name them accordingly:
    00_FirstPdf.pdf, 01_SecondPdf.pdf, etc.
    """
    pdfs_to_merge = get_pdf_in_folder(INPUT_FOLDER)

    merger = PdfFileMerger()

    for pdf in pdfs_to_merge:
        merger.append(pdf)

    output_path = os.path.join(OUTPUT_FOLDER, OUTPUT_NAME)
    merger.write(output_path)
    merger.close()
