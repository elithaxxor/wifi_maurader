# 🌟 Wi-Fi Maurader

Wi-Fi Maurader is a comprehensive toolkit designed for executing Wi-Fi penetration testing tasks. With features such as phishing portal management, rogue access point (Evil Twin) creation, credential collection, and packet analysis, this toolkit is an essential resource for cybersecurity professionals aiming to test and secure wireless networks.

<p align="center">
  <img src="https://img.shields.io/badge/WiFi-PenetrationTesting-blue?style=for-the-badge&logo=wifihotspot&logoColor=white" alt="Wi-Fi Penetration Testing"/>
  <img src="https://img.shields.io/badge/Tools-Toolkit-green?style=for-the-badge" alt="Toolkit"/>
  <img src="https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.x"/>
</p>

---

## 📋 Table of Contents

- [🌟 Overview](#-overview)
- [✨ Key Features](#-key-features)
- [🔧 Installation](#-installation)
- [🛠️ Usage](#-usage)
- [🧑‍🤝‍🧑 Contributing](#-contributing)
- [📜 License](#-license)

---

## 🌟 Overview

Wi-Fi Maurader provides cybersecurity professionals with a versatile set of tools to evaluate the security posture of wireless networks. By leveraging the capabilities provided by this toolkit, users can effectively simulate real-world attack scenarios, allowing for better defense mechanisms against malicious activities. 

**Key Functions Include:**
- Creating rogue access points to intercept network traffic.
- Managing phishing portals aimed at collecting user credentials.
- Analyzing packet data for in-depth network activity assessment.

---

## ✨ Key Features

### 1. Rogue Access Point (Evil Twin)
- **Create a Fake Access Point**: Easily set up a rogue access point with a customizable SSID.
- **Control Access Points**: Start and stop the access point through an intuitive GUI or API, allowing for flexible testing scenarios.

### 2. Phishing Portal Management
- **Manage Templates**: Create and manage phishing portal templates to execute social engineering attacks effectively.
- **Easy Activation**: Activate phishing templates effortlessly via the GUI or API, making it user-friendly for all skill levels.

### 3. Packet Capture
- **Analyze Network Activity**: Start and stop packet capture to closely analyze wireless network traffic.
- **Live Data View**: Monitor live packet data continuously, providing real-time insights into network behavior.

### 4. Credential Collection
- **Automatic Log Collection**: Collect and display credentials obtained from phishing attempts seamlessly, aiding in evaluating user awareness and response.

---

## 🔧 Installation

To get started with Wi-Fi Maurader, follow these simple installation steps:

### Step 1: Clone the Repository

```bash
git clone https://github.com/elithaxxor/wifi_maurader.git
cd wifi_maurader
```

### Step 2: Install Required Packages

Ensure you have Python 3.x installed, then install the dependencies necessary for running the toolkit:

```bash
pip install -r requirements.txt
```

### Step 3: Check System Requirements

Ensure your system has the necessary permissions and packages to run Wi-Fi Maurader:
- A compatible wireless adapter with monitor mode support.
- Administrative or root privileges for executing specific functions like packet capture and access point creation.

---

## 🛠️ Usage

Starting with Wi-Fi Maurader is easy! Once installed, you can execute the main application:

```bash
python main.py
```

### Primary Functions
- From the GUI, navigate to different sections to create rogue access points or manage phishing portals.
- Use the "Start Capture" button to begin monitoring packets and the "View Logs" option to analyze collected credentials.

### Example Workflow
1. **Create a Rogue Access Point**:
   - Select the "Evil Twin" tab and input your desired SSID.
   - Click "Start AP" to activate your rogue access point.

2. **Manage Phishing Portals**:
   - Navigate to the "Phishing" section.
   - Choose a template and click "Activate".

3. **Monitor Packets**:
   - Access the "Packet Capture" tab and click "Start Capture".

---

## 🧑‍🤝‍🧑 Contributing

Contributions to Wi-Fi Maurader are welcome! If you'd like to help improve the toolkit, please follow these guidelines:

1. **Fork the Repository**: Click on the "Fork" button in the top right corner.
2. **Create a Feature Branch**: Use a descriptive name for your branch.
3. **Make Your Changes**: Implement your changes and test thoroughly.
4. **Commit Your Changes**: Write a clear commit message describing your changes.
5. **Create a Pull Request**: Submit a pull request for review.

---

## 📜 License

This project is licensed under the MIT License. Please see the [LICENSE](LICENSE) file for more details.

---

Feel free to dive into the code, explore its capabilities, and help make Wi-Fi Maurader an even more powerful toolkit for Wi-Fi penetration testing! Happy testing! 🔒🚀
