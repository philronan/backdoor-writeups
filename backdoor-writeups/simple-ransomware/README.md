simple-ransomware
=================

Link: https://backdoor.sdslabs.co/challenges/Simple-Ransomware \
Tags: [n00b19CTF] [crypto]

Description:
------------

Someone's files have been encrypted using the same IV/key pair. One of the files contains a flag. Can you recover it?

Solution:
---------

The encryption program provided as reference is rather flawed. First of all, it uses and then discards a randomly generated 256-bit key that could never be recovered even if someone did pay the ransom.

But more importantly for us, it performs CTR-mode encryption with the same key and IV for every file. In this mode, the key and IV are used to generate a pseudo-random keystream that is XORed with the plaintext to produce the encrypted ciphertext. If we know what the plaintext was for one file, we can XOR it with the corresponding ciphertext to obtain the keystream, which can be used to decrypt other files.

At the time of writing, it's still possible to download [pycrypto-2.6.1.tar.gz](https://ftp.dlitz.net/pub/dlitz/crypto/pycrypto/), but just in case it isn't here are the first 34 bytes of this file:

```
00000000: 1f8b 0808 d471 5c52 02ff 6469 7374 2f70  .....q\R..dist/p
00000010: 7963 7279 7074 6f2d 322e 362e 312e 7461  ycrypto-2.6.1.ta
00000020: 7200                                     r.
```

You shouldn't have much trouble decrypting the flag with this information.
