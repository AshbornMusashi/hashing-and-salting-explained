import hashlib  # A library containing different hashing algorithms.

def hash_data(data):  # We create a function called hash_data.
    result = hashlib.sha256(data.encode())  # This is where the actual hashing occurs using SHA-256.
    return result.hexdigest()  # Converts the hash from raw bytes into a readable hexadecimal string.


print(hash_data("sunshine123"))  # We print out the hashed value.
