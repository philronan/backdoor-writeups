bites-the-encryption
====================

Link: https://backdoor.sdslabs.co/challenges/Bites-The-Encryption \
Tags: [crypto] [n00b20ctf]

Description:
------------

You are provided with a Base64-encoded message `msg.enc` that has been encrypted by a Python program `encrypt.py`. The encryption program looks like this:

```python
from Crypto.Cipher import AES
from base64 import b64encode
import os
import secert

key = os.urandom(16)
msg = secert.msg
nonce = b"     177013     " # dont google this

crypto = AES.new(key, AES.MODE_CTR, counter=lambda: nonce)
msg = crypto.encrypt(msg)
print(b64encode(msg))
```

Solution
--------

On the face of it, this looks like a difficult one to crack. When implemented correctly, AES in CTR mode should be impossible to decipher without the correct key. However, the `counter` parameter looks strange. This is supposed to be a function that returns an incrementing 128-bit value at each call, but instead it returns a constant string of 16 bytes. As a result, each 16-byte block of plaintext is effectively being encrypted with exactly the same key. We can therefore treat the ciphertext as a sort of XOR Vigenère cipher using an unknown 16-byte key.

While working on the [CryptoPals Crypto Challenge](https://cryptopals.com/), I created a tool that can crack repeating-key XOR ciphers quite successfully in cases where the plaintext consists of plain English. It certainly didn't have much trouble with this one:

```python
from cryptopals import vigenereCrack
ct = open('msg.enc','r').read().decode('base64')
print vigenereCrack(ct,keysize=16)
```
