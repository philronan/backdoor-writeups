rsanne
======

Link https//backdoor.sdslabs.co/challenges/RSANNE \
Tags [crypto] [backdoorctf15]

Description
------------

Extract a flag from an RSA-encrypted ciphertext and the RSA public key that was used to encrypt it.

Solution
---------

The public key looks very unusual

```
-----BEGIN PUBLIC KEY-----
MIICUjANBgkqhkiG9w0BAQEFAAOCAj8AMIICOgKCAjEP////////////////////
////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////
//////////////////////////3////////////4AAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAECAwEAAQ==
-----END PUBLIC KEY-----
```

Let's use Openssl to find out what the modulus and public exponent are

```
$ openssl rsa -pubin -in id_rsa.pub -text -noout
Public-Key (4484 bit)
Modulus
    0fffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffff
    fffffffffffdffffffffffffffffff
    f80000000000000000000000000000
    000000000000000000000000000000
    000000000000000000000000000000
    000000000000000000000000000000
    000000000000000000000000000000
    000000000000000000000000000000
    000000000000000000000000000000
    000000000000000000000000000000
    000000000000000000000000000000
    000000000000000000000000000000
    000000000000000000000000000000
    000000000000000000000000000000
    000000000000000000000000000000
    000000000000000000000000000000
    000000000000000000000000000000
    000000000000000000000000000000
    000000000000000000000000000000
    000000000000000000000000000000
    000000000001
Exponent 65537 (0x10001)
```

So many Fs! So many zeros! If you played around with pocket calculators a lot when you were a kid, you might recognise this sort of number.

```
9999 * 9999 = 99980001
99999 * 999 = 99899001
```

It looks like this modulus is the product of two numbers that consist entirely of 1s when written in binary. Let's put this idea to the test

```python
n = int('0fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff' \
        'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff' \
        'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff' \
        'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff' \
        'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff' \
        'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff' \
        'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff' \
        'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff' \
        'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff' \
        'fffffffffffdfffffffffffffffffff80000000000000000000000000000' \
        '000000000000000000000000000000000000000000000000000000000000' \
        '000000000000000000000000000000000000000000000000000000000000' \
        '000000000000000000000000000000000000000000000000000000000000' \
        '000000000000000000000000000000000000000000000000000000000000' \
        '000000000000000000000000000000000000000000000000000000000000' \
        '000000000000000000000000000000000000000000000000000000000000' \
        '000000000000000000000000000000000000000000000000000000000000' \
        '000000000000000000000000000000000000000000000000000000000000' \
        '000000000000000000000000000000000000000001', 16)
p = 3
while p < n and n%p > 0:
    p = (p << 1) | 1

if p < n:
    print("Success!")
    print("p=%#x" % p)
    print("q=%#x" % (n//p))
```

Well that was easy enough. But when I used these values of `p` and `q` to decrypt the ciphertext using the [textbook RSA](../_lib/textbook_rsa.py) code, I ended up with a load of random noise. Turns out that the plaintext has been padded, so we'll need to undo that as well.

```python
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

ciphertext = open('flag.enc').read().decode('base64')
n = p * q
e = 65537L
d = modinv(e, (p-1) * (q-1))
pkey = RSA.construct([n,e,d,p,q])
cipher = PKCS1_OAEP.new(pkey)
plaintext = cipher.decrypt(ciphertext)
print(plaintext)
```
