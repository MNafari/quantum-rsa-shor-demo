import time
import random
from math import gcd
from qiskit import Aer
from qiskit.utils import QuantumInstance
from qiskit.algorithms import Shor

def get_coprime(N):
    print("[*] Selecting random coprime of N...")
    attempts = 0
    while True:
        a = random.randint(2, N - 1)
        if gcd(a, N) == 1:
            print(f"    → Coprime found: a = {a}")
            return a
        attempts += 1
        if attempts > 1000:
            raise Exception("Too many attempts to find coprime.")

def main():
    N = 35  # You can change this to 15, 21, 35, etc.
    print("="*40)
    print(f"⚛️  Shor's Algorithm Simulation for N = {N}")
    print("="*40)

    # Step 1: Pick coprime 'a'
    a = get_coprime(N)

    # Step 2: Set up quantum backend
    print("[*] Setting up quantum simulator backend...")
    backend = Aer.get_backend("aer_simulator")
    quantum_instance = QuantumInstance(backend)

    # Step 3: Run Shor
    print("[*] Starting Shor's Algorithm quantum routine...")
    shor = Shor(quantum_instance=quantum_instance)

    start_time = time.time()

    try:
        result = shor.factor(N)
        end_time = time.time()

        print("\n🎯 Finished.")
        if result.factors:
            print(f"✅ Factors of {N} found: {result.factors}")
        else:
            print("❌ Shor's algorithm did not return valid factors this time.")
        print(f"⏱ Runtime: {end_time - start_time:.2f} seconds")
    except Exception as e:
        print("🚫 Error during execution:", str(e))

if __name__ == "__main__":
    main()

