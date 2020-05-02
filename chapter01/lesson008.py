def cipher_encrypt(s):
    return "".join([cipher(c) for c in s])

def cipher_decrypt(s):
        return "".join([cipher(c) for c in s])

def cipher(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return chr(219 - ord(c))
    else:
        return c

s1 = "Hello, world!"

s2 = cipher_encrypt(s1)
s3 = cipher_decrypt(s2)

print(s2)
print(s3)
