import zipfile
import string
import itertools

def brute_force_zip(zip_file_path):
    try:
        with zipfile.ZipFile(zip_file_path) as zip_file:
            characters = string.ascii_letters + string.digits + string.punctuation
            password_length = 1
            max_password_length = 10  # You can adjust this based on your requirements

            while password_length <= max_password_length:
                for combination in itertools.product(characters, repeat=password_length):
                    password = ''.join(combination)

                    try:
                        zip_file.extractall(pwd=password.encode())
                        print(f"Password found: {password}")
                        return
                    except Exception as e:
                        pass

                password_length += 1

            print("Password not found.")

    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    encrypted_zip_path = "path_to_encrypted_zip.zip"
    brute_force_zip(encrypted_zip_path)

