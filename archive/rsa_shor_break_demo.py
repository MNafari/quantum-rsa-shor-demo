import time
from math import gcd
from qiskit import Aer
from qiskit.utils import QuantumInstance
from qiskit.algorithms import Shor

# === RSA PART ===
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

message = 9
cipher = pow(message, e, n)
decrypted = pow(cipher, d, n)

print("=" * 40)
print("🔐 RSA Encryption & Decryption")
print("=" * 40)
print(f"p = {p}, q = {q}")
print(f"n = {n}, phi(n) = {phi_n}")
print(f"Public Key:  (e={e}, n={n})")
print(f"Private Key: (d={d}, n={n})")
print(f"Message = {message}")
print(f"Cipher  = {cipher}")
print(f"Decrypted = {decrypted}")

# === SHOR PART ===
print("\n⚛️ Running Shor's Algorithm to break RSA (n = 35)...")
start = time.time()

backend = Aer.get_backend("aer_simulator")
qi = QuantumInstance(backend)
shor = Shor(quantum_instance=qi)

try:
    result = shor.factor(n)
    end = time.time()
    print(f"\n🎯 Shor's Result:")
    print(f"  Factors of {n}: {result.factors}")
    print(f"⏱ Runtime: {end - start:.2f} seconds")
except Exception as e:
    print("🚫 Shor failed:", str(e))

