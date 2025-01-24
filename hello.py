import hashlib
import random
import string

def generate_random_string(length=32):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def find_hash_with_leading_zeros():
    for _ in range(1000):
        random_string = generate_random_string()
        hash_value = hashlib.sha256(random_string.encode()).hexdigest()
        if hash_value.startswith('00'):
            print(f"Hash found: {hash_value}")
            return True
    return False

if find_hash_with_leading_zeros():
    print("Hash with two consecutive zeros found within 1000 tries.")
else:
    print("No hash with two consecutive zeros found within 1000 tries.")
