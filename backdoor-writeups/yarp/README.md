yarp
====

Link: https://backdoor.sdslabs.co/challenges/YARP \
Tags: [crypto] [n00b20ctf]

Description:
------------

The linked file contains a straightforward RSA problem:

```
c = 10086629983555085122475300616286783004833619482...[309 digits in total]
n = 10361800278023047478364653956160509251716387678...[309 digits in total]
e = 177013
```

The modulus (`n`) is a 1024-bit number, so breaking it into its two prime factors could be difficult. But fortunately, its factors are available online at [factordb.com](http://factordb.com/index.php?id=1100000001430665739)

Solution
--------

Once we know `p` and `q`, the calculation is completely straightforward. Just calculate the decryption coefficient `d`, use it to decrypt `c`, then convert the resulting number into a string by treating its hexadecimal representation as a string of byte values. See `textbook_rsa.py` for details.

```
from textbook_rsa import rsa_decrypt
p = 13269061345880502955813507599576528235253714057... # (Numbers
q = 78089926694324611743126464868325115310742874375... # truncated
c = 10086629983555085122475300616286783004833619482... # for brevity)
e = 177013
print rsa_decrypt(p,q,c,e)
```
