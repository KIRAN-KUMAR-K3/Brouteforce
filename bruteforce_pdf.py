import PyPDF2

def open_encrypted_pdf(file_path, password):
    try:
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfFileReader(file)
            if pdf_reader.isEncrypted:
                with open(password, 'rb') as pass_file:
                    for line in pass_file:
                        password = line.strip()
                        if pdf_reader.decrypt(password) == 1:
                            print(f"PDF decrypted successfully. Password: {password.decode('utf-8')}")
                            break
                    else:
                        print("Unable to decrypt the PDF with the provided password.")
                        return
            else:
                print("The PDF is not encrypted.")

            num_pages = pdf_reader.getNumPages()
            print(f"The PDF contains {num_pages} pages.\n")

            for page_num in range(num_pages):
                page = pdf_reader.getPage(page_num)
                print(f"Page {page_num + 1}:")
                print(page.extractText())
                print("-" * 50)

    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    encrypted_pdf_path = "path_to_encrypted_pdf.pdf"
    password_file_path = "/usr/share/wordlists/rockyou.txt" #your_password_here

    open_encrypted_pdf(encrypted_pdf_path, password_file_path)
