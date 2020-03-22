frost
=====

Link: https://backdoor.sdslabs.co/challenges/FROST \
Tags: [n00b16CTF] [crypto]

Description:
------------

You're give a text file called `crypt.txt`, which consists of hexadecimal data. It's been encrypted with an unknown key.

Solution:
---------

The file contains 1626 characters, corresponding to 813 bytes of data. If it had been encrypted using a block cipher like AES, then we would have expected a number divisible by 16. So perhaps a stream cipher was used? Let's take a look at the distribution of values:

```python
>>> a = open('crypt.txt','r').read().decode('hex')
>>> print [a.count(chr(i)) for i in range(256)]
[3, 10, 4, 1, 2, 4, 4, 11, 0, 0, 4, 0, 0, 1, 1, 0, 2, 4, 7, 1, 3, 4, 10, 33, 1, 24, 2, 9,
9, 6, 1, 7, 18, 20, 2, 14, 14, 18, 7, 19, 9, 10, 18, 7, 16, 24, 15, 9, 13, 6, 4, 6, 0, 0,
10, 4, 13, 1, 7, 7, 8, 5, 3, 11, 8, 7, 6, 9, 6, 8, 0, 1, 0, 2, 6, 7, 1, 7, 6, 1, 6, 7, 9,
30, 5, 3, 17, 10, 19, 7, 3, 10, 12, 7, 7, 10, 1, 0, 0, 2, 19, 0, 2, 0, 23, 0, 2, 21, 0, 1,
0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 7, 1, 0, 0, 0, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

This isn't at all random. The values are almost entirely in the range from 0 to 127. A proper stream cipher like RC4 would have made a ciphertext almost indistinguishable from random noise, so we can rule that out. Perhaps this was encrypted with a repeating-key XOR cipher. I made [a tool to crack this sort of cipher](../_lib/cryptopals.py) while I was working on the [CryptoPals Crypto Challenge](https://cryptopals.com/). Turns out it was able to break this one in no time at all.

```
import cryptopals
print cryptopals.vigenereCrack(open('crypt.txt','r').read().decode('hex'))
```
