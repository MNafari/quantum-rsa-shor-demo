import streamlit as st
import time
from math import gcd
from qiskit import Aer
from qiskit.utils import QuantumInstance
from qiskit.algorithms import Shor

st.set_page_config(page_title="Quantum RSA Breaker", page_icon="🔐")

st.title("🔐 Quantum RSA Break Demo with Shor's Algorithm")
st.markdown("This educational app simulates **RSA encryption** and demonstrates how it can be broken using **Shor's Algorithm** on small numbers.")

# RSA Setup (fixed small primes for quantum demo)
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

# User Input
raw_input = st.text_input("🔤 Enter a number or short word (less than 35):")

if raw_input:
    try:
        if raw_input.isdigit():
            message = int(raw_input)
            input_type = 'number'
        else:
            message = int.from_bytes(raw_input.encode(), 'big')
            input_type = 'text'

        if message >= n:
            st.error("Message too large for n = 35. Only numbers < 35 are supported in this simulation.")
        else:
            cipher = pow(message, e, n)
            st.success(f"🔐 Encrypted → Cipher = {cipher}")

            if cipher == message:
                st.warning("⚠️ Cipher is equal to the original message.This happens because RSA encryption with small numbers can behave unexpectedly. In real-world RSA, large primes prevent this.")

            if st.button("⚛️ Run Shor's Algorithm to Break RSA"):
                backend = Aer.get_backend("aer_simulator")
                qi = QuantumInstance(backend)
                shor = Shor(quantum_instance=qi)

                with st.spinner("Running Shor..."):
                    start = time.time()
                    result = shor.factor(n)
                    end = time.time()

                factors = result.factors[0]
                if factors[0] * factors[1] == n:
                    st.success(f"🧮 Factors Found: {factors[0]} × {factors[1]} = {n}")

                    # Recalculate phi and d
                    p, q = factors
                    phi_n = (p - 1) * (q - 1)
                    d = modinv(e, phi_n)

                    recovered = pow(cipher, d, n)
                    if input_type == 'text':
                        recovered_text = recovered.to_bytes((recovered.bit_length() + 7) // 8, 'big').decode()
                        st.success(f"✅ Decrypted Text: {recovered_text}")
                    else:
                        st.success(f"✅ Decrypted Number: {recovered}")

                    st.info(f"⏱ Total runtime: {end - start:.2f} seconds")
                else:
                    st.error("❌ Shor failed to find valid factors.")

    except Exception as ex:
        st.error(f"Error: {str(ex)}")
