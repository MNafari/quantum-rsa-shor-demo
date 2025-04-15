
import time
from math import gcd
from qiskit import Aer
from qiskit.utils import QuantumInstance
from qiskit.algorithms import Shor

# === RSA SETUP ===
p = 5
q = 7
n = p * q
phi_n = (p - 1) * (q - 1)

def choose_e(phi_n):
    for e in range(2, phi_n):
        if gcd(e, phi_n) == 1:
            return e
    raise Exception("No valid e found")

def modinv(e, phi_n):
    for d in range(2, phi_n):
        if (d * e) % phi_n == 1:
            return d
    raise Exception("No modular inverse found")

e = choose_e(phi_n)
d = modinv(e, phi_n)

# === Get user input ===
raw_input = input("🔤 Enter a number or short word to encrypt: ").strip()

# Convert input to integer
if raw_input.isdigit():
    message = int(raw_input)
    input_type = 'number'
else:
    message = int.from_bytes(raw_input.encode(), 'big')
    input_type = 'text'

if message >= n:
    print("❌ Message too large for current key.")
    print("ℹ️  Note: Due to the experimental nature of this quantum demo,")
    print("    only numbers smaller than n = 35 can be encrypted and broken.")
    print("    This ensures it runs properly on a regular (non-quantum) computer.")
    exit(1)

# Encrypt
cipher = pow(message, e, n)
print(f"🔐 Encrypted → Cipher: {cipher}")

# === Simulate Shor's Algorithm ===
print("⚛️ Running Shor to break RSA...")
start = time.time()
backend = Aer.get_backend("aer_simulator")
qi = QuantumInstance(backend)
shor = Shor(quantum_instance=qi)

try:
    result = shor.factor(n)
    end = time.time()
    factors = result.factors[0]
    print(f"🧮 Factors found: {factors}")
    if factors[0] * factors[1] != n:
        print("❌ Invalid factors. Attack failed.")
        exit(1)

    # Reconstruct private key
    p, q = factors
    phi_n = (p - 1) * (q - 1)
    d = modinv(e, phi_n)

    # Decrypt
    recovered = pow(cipher, d, n)
    print(f"🔓 Recovered numeric message: {recovered}")

    if input_type == 'text':
        recovered_text = recovered.to_bytes((recovered.bit_length() + 7) // 8, 'big').decode()
        print(f"✅ Final Decrypted Text: {recovered_text}")
    else:
        print(f"✅ Final Decrypted Number: {recovered}")

    print(f"⏱ Total time: {end - start:.2f} seconds")

except Exception as ex:
    print("🚫 Error during quantum attack:", str(ex))
