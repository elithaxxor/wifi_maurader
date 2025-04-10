# modules/phishing_portal_loader.py
import os
import shutil
from pathlib import Path
from cryptography.fernet import Fernet

PORTAL_DIR = Path("./phishing_portal")
TEMPLATE_DIR = Path("./phishing_templates")
KEY_FILE = Path(".enc_key")

def prompt_passphrase():
    return input("Enter decryption passphrase: ")

def load_fernet_from_passphrase(pw: str):
    from base64 import urlsafe_b64encode
    import hashlib
    key = hashlib.sha256(pw.encode()).digest()
    return Fernet(urlsafe_b64encode(key))

class PortalTemplateManager:
    def __init__(self, portal_path=PORTAL_DIR, template_path=TEMPLATE_DIR):
        self.portal_path = portal_path
        self.template_path = template_path
        self.templates = self.discover_templates()
        self.fernet = None

    def discover_templates(self):
        templates = []
        if not self.template_path.exists():
            self.template_path.mkdir(parents=True)
        for folder in self.template_path.iterdir():
            if folder.is_dir() and any(p.suffix == ".enc" for p in folder.glob("*.enc")):
                templates.append(folder.name)
        return templates

    def list_templates(self):
        return self.templates

    def preview_template(self, name):
        preview_file = self.template_path / name / "preview.png"
        return preview_file if preview_file.exists() else None

    def decrypt_template(self, src: Path, dst: Path):
        with open(src, "rb") as f:
            encrypted = f.read()
        decrypted = self.fernet.decrypt(encrypted)
        with open(dst, "wb") as f:
            f.write(decrypted)

    def activate_template(self, name):
        selected_path = self.template_path / name
        if not selected_path.exists():
            raise FileNotFoundError(f"Template '{name}' not found.")

        passphrase = prompt_passphrase()
        self.fernet = load_fernet_from_passphrase(passphrase)

        if self.portal_path.exists():
            shutil.rmtree(self.portal_path)
        self.portal_path.mkdir(parents=True)

        for enc_file in selected_path.glob("*.enc"):
            target_file = self.portal_path / enc_file.stem  # remove .enc
            self.decrypt_template(enc_file, target_file)

        print(f"[*] Activated and decrypted phishing template: {name}")
