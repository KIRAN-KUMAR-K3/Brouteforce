from zipfile import ZipFile

def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password)
        return True
    except:
        return False

def main():
    print("[+] Beginning bruteforce ")
    with ZipFile('enc.zip') as zf:
        with open('/usr/share/wordlists/rockyou.txt', 'rb') as f: #your_password_list_goes_here
            for p in f:
                password = p.strip()
                if attempt_extract(zf, password):
                    print("[+] Correct password: %s" % password)
                    exit(0)
                else:
                    print("[-] Incorrect password: %s" % password)

    print("[+] Password not found in list")

if __name__ == "__main__":
    main()
