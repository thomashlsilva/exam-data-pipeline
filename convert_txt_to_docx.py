import os
from docx import Document


def convert_txt_to_docx(txt_folder, docx_folder):
    # Check if the output folder exists, if not, create it
    if not os.path.exists(docx_folder):
        os.makedirs(docx_folder)

    # Iterate through each file in the input folder
    for txt_file in os.listdir(txt_folder):
        if txt_file.endswith(".txt"):
            # Create a new Word document
            doc = Document()

            # Read the content from the text file and add it to the Word document
            with open(os.path.join(txt_folder, txt_file), "r", encoding="utf-8") as txt:
                doc.add_paragraph(txt.read())

            # Save the Word document with the same name in the output folder
            docx_file = os.path.join(docx_folder, os.path.splitext(txt_file)[0] + ".docx")
            doc.save(docx_file)


if __name__ == "__main__":
    # Specify the folder containing the text files and the folder for the output Word documents
    txt_folder_path = "./text"
    docx_folder_path = "./docx"

    convert_txt_to_docx(txt_folder_path, docx_folder_path)
