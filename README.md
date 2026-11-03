# Hashing and Salting Explained

Disclosure: This README turned out a little longer than expected, so don't worry if you don't remember everything. 
However, if there's one thing I hope you remember, it's this simple story:

Alice and Bob both use the password `sunshine123` on a website called CoolSite.

- **No hashing:** A hacker who breaks into the database can read both passwords.
- **Hashing:** The database stores hash values instead, but since the passwords match, so do the hash values. Crack one, and you know both.
- **Hashing + salting:** Each password gets its own random salt, so Alice and Bob end up with completely different hashes. 🎉


## 1. What is Hashing?

Hashing converts data of any size into a fixed-length string of characters using a **hash function**.

Think of a hash function as a machine: you put data in, and it gives you a fixed-length output called a **hash value**.

### Example

**Input:** `Hello`
**Hash function:** SHA-256
**Output:** 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969

Key properties of hashing:

- **One-way:** You can create a hash value from data, but you can't reverse it to get the original data.
- **Consistent:** The same input with the same hash function always gives the same hash value.
- **Fixed length:** SHA-256 always produces 64 hexadecimal characters, no matter how big the input is.
- **Sensitive to change:** Changing even one character (like `Hello` to `hello`) produces a completely different hash value.

Common hash functions include SHA-256, SHA-512, and SHA-3.

## 2. What is Salting?

A **salt** is a random value added to a password before it is hashed.

Why does this matter? Without salting, two users with the same password get identical hash values. Attackers can also use precomputed tables 
of hash values (called **rainbow tables**) to crack passwords quickly.

With a unique salt for each password, the hashes are always different, and precomputed tables become useless.

**Without salting:** Password → Hash Function → Hash Value

**With salting:** Password + Random Salt → Hash Function → Hash Value


Note:A salt does not need to be secret. It just needs to be random and unique for each password. It is usually stored right next to the hash value.

Hashing is one-way and can’t be reversed, so it’s used for storing passwords and checking data integrity.
Encryption is reversible with a key, so it’s used to protect data you need to read later.


### ⚠️ A Security Note

SHA-256 is fast, which helps attackers guess passwords quickly. Real websites should use **Argon2id, bcrypt, or scrypt** instead.

## Conclusion

Hashing turns data into fixed-length outputs, and salting adds extra protection when storing passwords. 
These concepts are a great starting point for learning about cryptography and security.

🎉 All contributions are welcome—feel free to fork the repo and submit a pull request anytime!
Thanks for reading
