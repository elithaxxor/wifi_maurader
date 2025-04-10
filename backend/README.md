# 🚀 API Server for Wi-Fi Penetration Testing

<div align="center">
  <img src="https://img.shields.io/badge/FastAPI-0.68.1-blue?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.x"/>
  <img src="https://img.shields.io/badge/CORS-enabled-brightgreen?style=for-the-badge&logo=browser&logoColor=white" alt="CORS Support"/>
</div>

<p align="center">
  <img src="https://raw.githubusercontent.com/elithaxxor/API_Server/main/assets/api_server_logo.png" alt="API Server Logo" width="300"/>
</p>

> 🌐 **API Server**: A backend server developed with FastAPI for managing Wi-Fi penetration testing functionalities, including phishing portals and packet capture.

---

## 📋 Table of Contents

- [🌟 Overview](#-overview)
- [✨ Key Features](#-key-features)
- [📂 Directory Structure](#-directory-structure)
- [🔧 Requirements](#-requirements)
- [🚀 Installation](#-installation)
- [🎮 Usage Guide](#-usage-guide)
- [📡 API Endpoints](#-api-endpoints)
- [🔄 Execution](#-execution)
- [🧑‍🤝‍🧑 Contributing](#-contributing)
- [📜 License](#-license)

---

## 🌟 Overview

The `api_server.py` file is a robust backend API server built using the FastAPI framework, designed specifically to facilitate Wi-Fi penetration testing. This server provides several critical functionalities such as phishing portal management, credential logging, and packet capturing, making it an essential tool for security professionals and ethical hackers.

---

## ✨ Key Features

- **🔗 API Endpoints**: Exposes multiple endpoints for managing Wi-Fi access points and phishing portals.
- **🛠️ Data Validation**: Utilizes Pydantic models for rigorous data validation ensuring data integrity and robustness.
- **🌐 CORS Support**: Configures CORS middleware to allow requests from any origin, facilitating easy interaction with web-based clients.
- **📥 Live Packet Capture**: Enables real-time packet capture functionality for monitoring network traffic.

---

## 📂 Directory Structure

```
api_server/
│
├── api_server.py           # Main FastAPI server file
├── modules/
│   ├── __init__.py        
│   ├── evil_twin_ap.py     # Handles Evil Twin AP functionalities
│   ├── portal_template.py   # Manages phishing portal templates
│   └── packet_capture.py     # Packet capturing functionalities
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## 🔧 Requirements

Before running the API server, ensure you have the following installed:

- 🐍 Python 3.6 or higher
- 📦 FastAPI
- 🎒 Uvicorn (for serving ASGI applications)
- 🔀 CORS (for Cross-Origin Resource Sharing)
- 🔍 Pydantic (for data validation)

Use the `requirements.txt` to install the required packages:

```bash
pip install -r requirements.txt
```

---

## 🚀 Installation

To set up the API server, follow these steps:

### Step 1: Clone the Repository

```bash
git clone https://github.com/elithaxxor/API_Server.git
cd API_Server
```

### Step 2: Install Required Packages

```bash
pip install -r requirements.txt
```

### Step 3: Check Python Version

Ensure you are using Python 3.6 or later:

```bash
python --version
```

---

## 🎮 Usage Guide

### Running the API Server

To run the API server, execute the following command in your terminal:

```bash
uvicorn api_server:app --host=0.0.0.0 --port=8000 --reload
```

- This command starts the FastAPI application with hot-reload capabilities, allowing you to see changes instantly.

---

## 📡 API Endpoints

The following API endpoints are available for managing Wi-Fi penetration testing features:

| Endpoint                             | Method   | Description                                                   |
|-------------------------------------|----------|---------------------------------------------------------------|
| **`/api/templates`**                | `GET`    | Retrieves a list of available phishing portal templates.     |
| **`/api/activate_template`**        | `POST`   | Activates a specified phishing portal template.              |
| **`/api/start_ap`**                 | `POST`   | Starts an access point (AP) with a given SSID.              |
| **`/api/stop_ap`**                  | `POST`   | Stops the currently running access point.                    |
| **`/api/creds`**                    | `GET`    | Fetches credential logs from a designated directory.         |
| **`/api/packet_capture/start`**     | `POST`   | Starts packet capture and enables monitor mode.              |
| **`/api/packet_capture/stop`**      | `POST`   | Stops packet capture and disables monitor mode.              |
| **`/api/packet_capture/live`**      | `GET`    | Provides live packet data in real-time.                      |

### Example Request

Here’s how you can activate a phishing template using a POST request:

```bash
curl -X POST "http://localhost:8000/api/activate_template" -H "Content-Type: application/json" -d '{"template_id": "example_template"}'
```

---

## 🔄 Execution

The API server is designed to run on the following configuration:

- **Host**: `0.0.0.0`
- **Port**: `8000`

This setup allows the server to be accessible from any network interface, making it convenient for both local and remote access.

---

## 🧑‍🤝‍🧑 Contributing

Contributions to the API server repository are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push to your forked repository.
5. Create a pull request describing your changes.

Together, we can enhance the functionality and capabilities of this project!

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to reach out with any questions or suggestions regarding this API server and its functionalities! Happy hacking! 🔒✨
