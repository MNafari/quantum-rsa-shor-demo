# ⚙️ Setup Instructions for Quantum RSA Break Demo

This guide helps you run the project step by step on a Linux system.

---

## ✅ Prerequisites

- Operating System: **Linux (Ubuntu recommended)**
- Python version: **Python 3.10+**
- Git (optional, for cloning repo)

---

## 📦 1. Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 🐍 2. Upgrade pip

```bash
pip install --upgrade pip
```

---

## 📦 3. Install Required Python Packages

```bash
pip install -r requirements.txt
```

This will install Qiskit and its dependencies including:

- Aer (simulator)
- Algorithms (Shor)
- Visualization tools (optional)

---

## ▶️ 4. Run the Main Demo

```bash
python rsa_shor_input_demo_final.py
```

You will be prompted to enter a **number or short word**.  
⚠️ Due to simulation limits, only numbers **less than 35** are supported.

---

## 🧪 Example Run

```
🔤 Enter a number or short word to encrypt: 7
🔐 Encrypted → Cipher: 29
⚛️ Running Shor to break RSA...
🧮 Factors found: [5, 7]
🔓 Recovered numeric message: 7
✅ Final Decrypted Number: 7
```

---

## 🧹 Optional: Ignore Files in Git

Create a `.gitignore` file:

```
venv/
__pycache__/
*.pyc
```

---

Enjoy quantum hacking — responsibly 😄