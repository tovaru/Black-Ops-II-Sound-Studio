from Crypto.Cipher import Salsa20
import base64
import os, sys

secret_base64 = "kZLU3vLqN1jnSgDBFiEmRguT0O1u7dxk2CGrqRReL8lKG7ECAAAAAA=="
secret_base64_bytes = secret_base64.encode()
secret = base64.b64decode(secret_base64_bytes)[:32]
secret_nonce = base64.b64decode(secret_base64_bytes)[32:]

# get decrpyted input file path
path = sys.argv[1]

# make output path
basename = os.path.basename(path)
dirname = os.path.dirname(path)
output_name = os.path.splitext(basename)[0]
output_format = os.path.splitext(basename)[1]
output_basename = output_name + ".encrypted" + output_format
output_path = os.path.join(dirname, output_basename)

# load decrypted file
print("Loading file...")
with open(path, "rb") as enc_file:
    file = enc_file.read()

# encrypt file
print("Encrypting...")
cipher = Salsa20.new(key=secret, nonce=secret_nonce)
encrypted = cipher.encrypt(file)

# save encrypted file
print(f"Saving file to {output_path}...")
with open(output_path, "wb") as dec_file:
    dec_file.write(encrypted)

print("File encrypted succesfully!")
