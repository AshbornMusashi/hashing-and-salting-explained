# A library containing different hashing algorithms.
import hashlib 

# We create a function called hash_data.
def hash_data(data):  
     # This is where the actual hashing occurs using SHA-256.
    result = hashlib.sha256(data.encode())
    # Converts the hash from raw bytes into a readable hexadecimal string.
    return result.hexdigest()  

# We print out the hashed value.
print(hash_data("sunshine123"))  
