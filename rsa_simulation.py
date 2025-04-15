from math import gcd

# Step 1: Choose two primes that Shor can break
p = 5
q = 7
n = p * q
phi_n = (p - 1) * (q - 1)

# Step 2: Choose e
def choose_e(phi_n):
    for e in range(2, phi_n):
        if gcd(e, phi_n) == 1:
            return e
    raise Exception("No valid e found")

e = choose_e(phi_n)

# Step 3: Compute modular inverse d
def modinv(e, phi_n):
    for d in range(2, phi_n):
        if (d * e) % phi_n == 1:
            return d
    raise Exception("No modular inverse found")

d = modinv(e, phi_n)

# Step 4: Encrypt message
message = 9
cipher = pow(message, e, n)
decrypted = pow(cipher, d, n)

print("🔐 RSA ENCRYPTION")
print(f"  p = {p}, q = {q}")
print(f"  n = {n}, phi(n) = {phi_n}")
print(f"  Public key: (e={e}, n={n})")
print(f"  Private key: (d={d}, n={n})")
print(f"  Message = {message}")
print(f"  Cipher  = {cipher}")
print(f"  Decrypted = {decrypted}")

