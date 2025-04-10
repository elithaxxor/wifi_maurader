import tkinter as tk
from tkinter import ttk, messagebox
from modules.evil_twin import EvilTwinAP
from modules.phishing_portal_loader import PortalTemplateManager

class WiFiAttackGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Wi-Fi Attack Toolkit")
        self.root.geometry("600x400")

        self.evil_ap = EvilTwinAP()
        self.template_manager = PortalTemplateManager()

        self.ssid_var = tk.StringVar(value=self.evil_ap.ssid)
        self.template_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="SSID to Broadcast:").pack(pady=5)
        ttk.Entry(self.root, textvariable=self.ssid_var, width=30).pack()

        ttk.Label(self.root, text="Phishing Template:").pack(pady=5)
        template_box = ttk.Combobox(self.root, textvariable=self.template_var, values=self.template_manager.list_templates())
        template_box.pack()

        ttk.Button(self.root, text="Activate Template", command=self.activate_template).pack(pady=5)
        ttk.Button(self.root, text="Start Evil Twin AP", command=self.start_evil_ap).pack(pady=10)
        ttk.Button(self.root, text="Stop Evil Twin AP", command=self.stop_evil_ap).pack(pady=5)

    def activate_template(self):
        try:
            self.template_manager.activate_template(self.template_var.get())
            messagebox.showinfo("Template Activated", f"Activated {self.template_var.get()}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def start_evil_ap(self):
        self.evil_ap.ssid = self.ssid_var.get()
        self.evil_ap.start()
        messagebox.showinfo("Started", f"Rogue AP '{self.ssid_var.get()}' is now live.")

    def stop_evil_ap(self):
        self.evil_ap.stop()
        messagebox.showinfo("Stopped", "Evil Twin AP has been stopped.")

if __name__ == '__main__':
    root = tk.Tk()
    app = WiFiAttackGUI(root)
    root.mainloop()
