# This program extracts cover (first) page from Pybook2 and merges the cover
# with preliminary pages (Pybook1) and rest of the book content (Pybook2)

from pypdf import PdfWriter, PdfReader
from pathlib import Path

home = Path.home()

# Convert paths to the books into pathlib Path objects
pybook = home / "Downloads" / "Pybook.pdf"
pybook2 = home / "Downloads" / "Pybook2.pdf"


# Pybook2 has the cover page but Pybook1 (preliminary) does not.
# Read and extract cover page from Pybook2 as a single PdfWriter object.
# Here, there is no need to write the extracted cover to a file
pybook2_reader = PdfReader(pybook2)
cover = pybook2_reader.pages[0]
cover_page = PdfWriter()
cover_page.add_page(cover)

# Extract pages in Pybook2, excluding the first (cover) page
pybook2_content = pybook2_reader.pages[1:]

# write pages in pybook2 to a PdfWriter object
pybook2 = PdfWriter()
for page in pybook2_content:
    pybook2.add_page(page)


# merge cover_page object, pybook file, and pybook2 file in that order
list_of_pdf = [cover_page, pybook, pybook2]
merger = PdfWriter()
for file_or_obj in list_of_pdf:
    merger.append(file_or_obj)
    print(f"{file_or_obj} added")

# write merged files and object to a new file
merger.write(
    home
    / "Desktop"
    / "py"
    / "books"
    / "Python Book.pdf"
)
print(
    f"Files/objects {list_of_pdf[0]}, {list_of_pdf[1]}, and {list_of_pdf[2]} merged successfully"
)
merger.close()
