from base64 import b64decode,b64encode
import json
from Crypto import Random
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


# Use this to get salt = Random.get_random_bytes(16)
salt = b'********'
masterhash = '******************'

def gen_vault_key(master_hash):
    vault_key = PBKDF2(master_hash, salt, 32, count=1000)
    return vault_key


def encypt(master_hash, plaintext):
    vault_key = gen_vault_key(master_hash)

    cipher = AES.new(vault_key, AES.MODE_EAX)
    iv = cipher.nonce

    # Padding the encoded plaintext
    data = pad(plaintext, AES.block_size)

    cipertext_bytes, tag = cipher.encrypt_and_digest(data)
    add_iv = cipertext_bytes + iv

    ciphertext = b64encode(add_iv).decode("utf-8")

    return ciphertext
    
def check(given_master_hash):
    if given_master_hash == masterhash:
        return True
    return False

def decrypt(master_key_given, cipher):
    ciphertext = b64decode(cipher)
    
    flag  = check(master_key_given)
    if (flag):
        key = gen_vault_key(master_key_given)
        iv = ciphertext[-16:]
        cipher = AES.new(key, AES.MODE_EAX, iv)
        password = unpad(cipher.decrypt(ciphertext[:-16]), AES.block_size)
        return password.decode()
    
    return False
    
# Returns masterkey hash in string format  
def master_hash_gen(masterkey):
    master_hash = hashlib.sha256(masterkey).hexdigest()
    return str(master_hash)
