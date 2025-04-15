import random
from math import gcd
from qiskit import Aer
from qiskit.utils import QuantumInstance
from qiskit.algorithms import Shor


# === RSA FUNCTIONS ===
def choose_e(phi_n):
    for e in range(2, phi_n):
        if gcd(e, phi_n) == 1:
            return e
    raise Exception("No valid 'e' found")

def modinv(e, phi_n):
    for d in range(2, phi_n):
        if (d * e) % phi_n == 1:
            return d
    raise Exception("No modular inverse found")

def rsa_generate_keys(p, q):
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = choose_e(phi_n)
    d = modinv(e, phi_n)
    return (e, d, n)

def rsa_encrypt(m, e, n):
    return pow(m, e, n)

def rsa_decrypt(c, d, n):
    return pow(c, d, n)


# === SHOR SIMULATION ===
def run_shor_simulation(n):
    backend = Aer.get_backend("aer_simulator")
    quantum_instance = QuantumInstance(backend)
    shor = Shor(quantum_instance=quantum_instance)
    try:
        result = shor.factor(n)
        return result.factors
    except Exception as ex:
        return str(ex)


# === MAIN INTERFACE ===
def main():
    print("="*30)
    print("🔐 RSA + Shor Quantum Demo")
    print("="*30)

    # Choose fixed small primes (RSA part)
    p, q = 11, 13  # n = 143
    e, d, n = rsa_generate_keys(p, q)

    try:
        msg = int(input("Enter a number to encrypt (less than {}): ".format(n)))
        if msg >= n:
            print("❌ Message must be less than n.")
            return
    except:
        print("❌ Invalid input.")
        return

    cipher = rsa_encrypt(msg, e, n)
    decrypted = rsa_decrypt(cipher, d, n)

    print("\n🔑 RSA KEYS:")
    print(f"  Public Key: (n={n}, e={e})")
    print(f"  Private Key: (n={n}, d={d})")

    print("\n📦 Encrypted message:", cipher)
    print("✅ Decrypted message:", decrypted)

    # Show Shor simulation (on small number like 15)
    print("\n⚛️ Simulating Shor's Algorithm on n = 15...")
    shor_factors = run_shor_simulation(15)

    print("🧮 Factors found for 15:", shor_factors)

    print("\n🚀 Done.")

if __name__ == "__main__":
    main()

