
# 🔐 Quantum RSA Break Demo (Shor Algorithm)

This is an educational, experiment-oriented project demonstrating how **RSA encryption** can be broken by a **quantum algorithm** called **Shor's Algorithm**, simulated using IBM's Qiskit library.

---

## 🧠 How It Works

1. A number or short word is encrypted using classical RSA.
2. The public modulus `n = p * q` is set to a small number (e.g., 35), small enough for quantum simulation.
3. Shor's Algorithm is run to find the prime factors of `n`.
4. If successful, the program recovers the private key and decrypts the original message.

---

## ⚠️ Limitations

Due to the computational complexity of quantum simulations on classical hardware:

- Only **small numbers** (< 35) can be encrypted and broken.
- Larger inputs will be rejected with a helpful message.
- Real-world RSA keys are **thousands of bits** and require real quantum hardware to be broken.

---

## ▶️ How to Run

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the main demo

```bash
python rsa_shor_input_demo_final.py
```

You will be prompted to enter a number or a short word to encrypt.

---

## 📁 Project Structure

```
.
├── rsa_shor_input_demo_final.py  # Main demo file
├── rsa_simulation.py             # Classical RSA example
├── shor_algorithm_sim.py         # Standalone Shor algorithm
├── requirements.txt              # Needed Python packages
├── images/                       # Screenshots for README
├── data/                         # Optional sample files
└── archive/                      # Older or experimental versions
```

---

## 🧪 Example

```
🔤 Enter a number or short word to encrypt: 8
🔐 Encrypted → Cipher: 34
⚛️ Running Shor to break RSA...
🧮 Factors found: [5, 7]
🔓 Recovered numeric message: 8
✅ Final Decrypted Number: 8
```

---

## 📚 Educational Purpose

This project is built for:

- Students learning about cryptography
- Researchers exploring quantum computing
- Instructors needing a live RSA+Shor demo

Enjoy breaking encryption — safely 😉
