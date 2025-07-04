def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_key_sequence(key, length):
    start = key % 100
    primes = []
    num = start
    while len(primes) < length:
        if is_prime(num):
            primes.append(num)
        num += 1
    return [(p % key) % 127 for p in primes]

def encrypt(plaintext, key):
    key_seq = generate_key_sequence(key, len(plaintext))
    ciphertext = ""
    for p, k in zip(plaintext, key_seq):
        p_val = ord(p)
        c = (p_val | k) % 127
        if c < 32:
            c += 32
        ciphertext += chr(c)
    return ciphertext

def decrypt(ciphertext, key):
    key_seq = generate_key_sequence(key, len(ciphertext))
    plaintext = ""
    for c, k in zip(ciphertext, key_seq):
        c_val = ord(c)
        t = c_val if c_val >= 32 else c_val - 32
        p = (t - k) % 127
        if p < 0:
            p += 127
        # Adjust p to satisfy encryption equation
        while ((p | k) % 127) != t:
            p = (p - 127) % 127
        plaintext += chr(p)
    return plaintext

# Test case
if __name__ == "__main__":
    plaintext = "Hello"
    key = 12345
    print(f"Plaintext: {plaintext}")
    ciphertext = encrypt(plaintext, key)
    print(f"Ciphertext: {ciphertext}")
    decrypted = decrypt(ciphertext, key)
    print(f"Decrypted: {decrypted}")
