# encrypt_portals.py
from cryptography.fernet import Fernet
import os
from pathlib import Path

TEMPLATE_DIR = Path("./phishing_templates")
KEY_FILE = Path(".enc_key")


def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    return key


def load_key():
    if not KEY_FILE.exists():
        return generate_key()
    return open(KEY_FILE, "rb").read()


def encrypt_folder(folder: Path, key: bytes):
    fernet = Fernet(key)
    for root, _, files in os.walk(folder):
        for name in files:
            if name.endswith(".enc"):
                continue
            file_path = Path(root) / name
            with open(file_path, "rb") as f:
                data = f.read()
            encrypted_data = fernet.encrypt(data)
            enc_path = file_path.with_suffix(file_path.suffix + ".enc")
            with open(enc_path, "wb") as f:
                f.write(encrypted_data)
            print(f"Encrypted {file_path} -> {enc_path}")


def main():
    key = load_key()
    for template in TEMPLATE_DIR.iterdir():
        if template.is_dir():
            encrypt_folder(template, key)


if __name__ == "__main__":
    main()
