import hashlib  # Library containing hashing algorithms.
import random   # Library for generating random values.

def hash_data(data, salt):
    result = hashlib.sha256((data + salt).encode())  # Combine the data and salt before hashing.
    return result.hexdigest()  # Convert the hash into a readable hexadecimal string.


password = "sunshine123"

# Generate two different salts.
salt1 = str(random.randint(0, 999))
salt2 = str(random.randint(0, 999))

# Hash the same password using different salts.
print("SpongeBob's hash:", hash_data(password, salt1))
print("Batman's hash:", hash_data(password, salt2))
