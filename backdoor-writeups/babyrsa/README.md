babyrsa
=======

Link: https://backdoor.sdslabs.co/challenges/BabyRSA \
Tags: [n00b19CTF] [crypto]

Description:
------------

You're given an encrypted flag and an RSA public key. Can you retrieve the flag?

Solution:
---------

The file `pub.pem` is a fairly ordinary-looking public key, but let's see what OpenSSL makes of it:

```
$ openssl rsa -pubin -in pub.pem -text
Public-Key: (1024 bit)
Modulus:
    00:e3:33:61:91:61:8b:b4:ce:32:a4:3a:9e:8e:e3:
    ad:18:1d:94:25:34:a4:9d:42:42:21:b7:ab:ba:77:
    55:27:6b:9e:b1:40:7a:d0:b2:20:42:9a:d5:c4:73:
    02:2a:5c:c9:3c:7e:12:69:88:4f:c5:d4:6c:e7:f3:
    0a:46:7a:79:66:50:2b:b5:ad:3c:0e:5c:66:f2:87:
    3a:c1:fb:5b:1d:0c:4e:ba:f9:9c:91:af:a8:f6:35:
    d6:d4:8a:ad:cf:fd:4f:b1:97:20:6c:30:be:cb:dd:
    6b:46:1f:65:07:b2:b4:1b:70:c6:d1:c1:26:98:a4:
    51:c9:92:26:b3:a9:13:69:21
Exponent: 3 (0x3)
writing RSA key
-----BEGIN PUBLIC KEY-----
MIGdMA0GCSqGSIb3DQEBAQUAA4GLADCBhwKBgQDjM2GRYYu0zjKkOp6O460YHZQl
NKSdQkIht6u6d1Una56xQHrQsiBCmtXEcwIqXMk8fhJpiE/F1Gzn8wpGenlmUCu1
rTwOXGbyhzrB+1sdDE66+ZyRr6j2NdbUiq3P/U+xlyBsML7L3WtGH2UHsrQbcMbR
wSaYpFHJkiazqRNpIQIBAw==
-----END PUBLIC KEY-----
```

The public exponent of 3 is unusually small. Normally the exponent is 65537. When using a small public exponent in textbook RSA (i.e., without any randomised padding of the plaintext), it's sometimes possible to decrypt a ciphertext simply by calculating its *e*-th root (in this case, the cube root). In such cases, the ciphertext is often considerably smaller than the modulus. And this case is no exception. The encrypted ciphertext (0x4a84229517afd6b5...etc...) has only 1003 bits, which is highly unusual.

So to retrieve the flag, just convert the `text.enc` file to a hex number and calculate its [cube root](https://stackoverflow.com/q/356090/1679849). Write the resulting number in hexadecimal, and convert each pair of hex digits to an ASCII character.
