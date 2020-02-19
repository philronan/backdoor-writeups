x0r-s33d-x0r
============

Link: https://backdoor.sdslabs.co/challenges/x0r-s33d-x0r \
Tags: [n00b19CTF] [reversing]

Description:
------------

Reverse the encryption applied to a ciphertext. The encryption algorithm is as follows:

1. Generate a random key value (from 1 to 999)

2. Use this value to seed Python's built-in random number generator

3. Generate a series of numbers (*x*<sub>1</sub>, *x*<sub>2</sub>, *x*<sub>3</sub>, ..., *x*<sub>*n*</sub>), where *x*<sub>*i*</sub> is equal to *i* XORed with the *i*-th output of `random.randint(1,1000))` after seeding the random number generator.

4. For each byte of plaintext, XOR its ASCII value with the corresponding value *x*<sub>*i*</sub>, and convert the resulting value into an 8-bit binary number.

5. Concatenate all these binary numbers, encode the resulting string as hexadecimal (so '1' and '0' become '31' and '30'), and then convert this string from hexadecimal into a decimal number.

Solution:
---------

Converting the ciphertext back into a sequence of byte values is completely straightforward:

```Python
ciphertext = 37984586344789065507651464464550655728857088937572544657 # ...etc...
bintext = ("%x" % ciphertext).decode('hex')
byte_vals = [int(bintext[i:i+8],2) for i in range(0,len(bintext),8)]
```

Since XOR encryption is reversible, you can decrypt the flag by XORing these values with the random sequence bytes in the same way as during encryption. All you need is the right value of `d`. But there are only 999 possible keys, and only one of them gives you a plaintext that starts with `CTF{`. So just try all of them.
