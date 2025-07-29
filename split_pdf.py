import os
import argparse
from pypdf import PdfReader, PdfWriter

def split_pdf(path: str, chunk_size: int = 100, output_dir: str = None) -> None:
    """
    Splits a PDF into smaller PDFs of `chunk_size` pages each.

    :param path: Path to the source PDF file.
    :param chunk_size: Number of pages per split file.
    :param output_dir: Directory to save split PDFs (defaults to current working directory).
    """
    if output_dir is None:
        output_dir = os.getcwd()

    reader = PdfReader(path)
    total_pages = len(reader.pages)
    base_name = os.path.splitext(os.path.basename(path))[0]

    for start in range(0, total_pages, chunk_size):
        writer = PdfWriter()
        end = min(start + chunk_size, total_pages)
        # Add pages [start, end)
        for page_num in range(start, end):
            writer.add_page(reader.pages[page_num])

        output_filename = f"{base_name}_pages_{start+1}_to_{end}.pdf"
        output_path = os.path.join(output_dir, output_filename)
        with open(output_path, "wb") as f_out:
            writer.write(f_out)
        print(f"Created: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Split one or more PDF files into chunks of N pages each."
    )
    parser.add_argument(
        "pdf_files",
        nargs='+',
        help="List of PDF files to split (e.g. file1.pdf file2.pdf)"
    )
    parser.add_argument(
        "-n", "--chunk_size",
        type=int,
        default=100,
        help="Number of pages per split file (default: 100)"
    )
    parser.add_argument(
        "-o", "--output",
        default=None,
        help="Output directory for split PDFs (default: current directory)"
    )
    args = parser.parse_args()

    for pdf_path in args.pdf_files:
        if not os.path.isfile(pdf_path):
            print(f"File not found: {pdf_path}")
            continue
        try:
            split_pdf(pdf_path, chunk_size=args.chunk_size, output_dir=args.output)
        except Exception as e:
            print(f"Error splitting {pdf_path}: {e}")

if __name__ == "__main__":
    main()
