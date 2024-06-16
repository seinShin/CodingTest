import hashlib

input = input()
encoded = input.encode()
rst = hashlib.sha256(encoded).hexdigest()
print(rst)