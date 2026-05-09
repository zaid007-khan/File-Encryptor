from cryptography.fernet import Fernet

# Generate key
key = Fernet.generate_key()

# Save key into a file
with open("secret.key", "wb") as key_file:
    key_file.write(key)

# Load key
with open("secret.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

# Create sample message file
with open("message.txt", "w") as file:
    file.write("This is a secret message.")

# Read original file
with open("message.txt", "rb") as file:
    original_data = file.read()

# Encrypt data
encrypted_data = cipher.encrypt(original_data)

# Save encrypted data
with open("encrypted.txt", "wb") as file:
    file.write(encrypted_data)

print("File encrypted successfully!")

# Decrypt data
decrypted_data = cipher.decrypt(encrypted_data)

# Save decrypted data
with open("decrypted.txt", "wb") as file:
    file.write(decrypted_data)

print("File decrypted successfully!")