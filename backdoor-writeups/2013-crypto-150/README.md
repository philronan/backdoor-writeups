2013-crypto-150
===============

Link: https://backdoor.sdslabs.co/challenges/2013-CRYPTO-150 \
Tags: [crypto]

Description:
------------

Extract a flag from a file encrypted using an unknown method.

Solution:
---------

The unknown method turns out to be repeating-key XOR encryption. Let's assume the plaintext message starts with the word "The". If this is true, then we can obtain the first four bytes of the key as follows. (I've omitted most of the ciphertext bytes; you can easily fill them in yourself.)

```
>>> ciphertext = '251f00522c3627490000...031f095a140204050b43'.decode('hex')
>>> plaintext = 'The '
>>> key = ''.join(chr(ord(p)^ord(q)) for (p,q) in zip(ciphertext,plaintext))
>>> print key
qwer
```

If that's what the key starts with, then it's easy to guess how it might continue...

```
>>> ciphertext = '251f00522c3627490000...031f095a140204050b43'.decode('hex')
>>> key = 'qwertyuiop'
>>> plaintext = ''.join(chr(ord(p)^ord(q)) for (p,q) in zip(ciphertext,key))
>>> print plaintext
The XOR op
```

We're definitely on the right track. Let's find out what the next part of the key is:

```
>>> ciphertext = '251f00522c3627490000...031f095a140204050b43'.decode('hex')
>>> plaintext = 'The XOR operator '
>>> key = ''.join(chr(ord(p)^ord(q)) for (p,q) in zip(ciphertext,plaintext))
>>> print key
qwertyuiopasdfghj
```

It should by now be perfectly obvious where this is heading. The flag is near the end of the plaintext.
