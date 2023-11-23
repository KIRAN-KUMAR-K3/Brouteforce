import PyPDF2
import string
import itertools

def brute_force_pdf(file_path):
    try:
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfFileReader(file)

            if pdf_reader.isEncrypted:
                characters = string.ascii_letters + string.digits + string.punctuation
                password_length = 1
                max_password_length = 10  # You can adjust this based on your requirements

                while password_length <= max_password_length:
                    for combination in itertools.product(characters, repeat=password_length):
                        password = ''.join(combination)

                        if pdf_reader.decrypt(password) == 1:
                            print(f"Password found: {password}")
                            num_pages = pdf_reader.getNumPages()
                            print(f"The PDF contains {num_pages} pages.\n")

                            for page_num in range(num_pages):
                                page = pdf_reader.getPage(page_num)
                                print(f"Page {page_num + 1}:")
                                print(page.extractText())
                                print("-" * 50)
                            return

                    password_length += 1

                print("Password not found.")

            else:
                print("The PDF is not encrypted.")

    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    encrypted_pdf_path = "path_to_encrypted_pdf.pdf"
    brute_force_pdf(encrypted_pdf_path)

