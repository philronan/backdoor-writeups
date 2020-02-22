c0ll1s10n-it-is
===============

Link: https://backdoor.sdslabs.co/challenges/c0ll1s10n-It-is \
Tags: none

Description:
------------

Find two different strings that produce a collision in a hash function.

Solution:
---------

The challenge has to be solved at an online server that is currently offline. However, its source code is still available. If you strip away the extraneous functions that input two strings and check that they are of equal length (at least 6 characters), the hash function itself looks like this:

```python
import binascii

def calculate_Hash(text):
        var1 = bin(int(binascii.hexlify(text),16))[2:]
        var2 = var1[1::2]
        var3 = var1[-1:]
        var4 = int(var2,2) ^ int(var3,2)
        var5 = '{0:b}'.format(var4)
        var6 = var5[-3:]+var5[0]
        var7 = int(var6, 2)
        var8 = n00b_confused(var7)
        return var8

def n00b_confused(n):
        s = 0
        while n:
                s += n % 10
                n //= 10
        return s
```

Instead of trying to pull this algorithm apart, I just wrote a program to generate 6-character strings and find two that had the same hash value. Using sequential numbers starting from 100000, this took no time at all to find a collision.
