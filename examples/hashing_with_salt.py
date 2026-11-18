# Library containing hashing algorithms.
import hashlib  
# Library for generating random values.
import random   

def hash_data(data, salt):
    # Combine the data and salt before hashing.
    result = hashlib.sha256((data + salt).encode())
    # Convert the hash into a readable hexadecimal string.
    return result.hexdigest()  

#a random password stored in a variable
password = "sunshine123"

# Generate two different salts.
salt1 = str(random.randint(0, 999))
salt2 = str(random.randint(0, 999))

# Hash the same password using different salts.
print("SpongeBob's hash:", hash_data(password, salt1))
print("Batman's hash:", hash_data(password, salt2))
