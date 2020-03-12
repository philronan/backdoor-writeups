rsalot
======

Link https://backdoor.sdslabs.co/challenges/RSALOT \
Tags [crypto] [backdoorctf15]

Description
------------

You're given a compressed archive file that contains many different RSA public keys and a single base64-encoded ciphertext. Decrypt it to obtain a flag.

Solution
---------

These look like proper RSA keys. They all have a 2048-bit modulus and a public exponent of 65537. But why so many? Let's start by extracting all the modulus values:

```
$ for f in *.pem
  do
    openssl rsa -pubin -in $f -noout -modulus | sed s/Modulus=/0x/
  done >mods.txt
```

Perhaps some of these share a common factor? Let's write some Python to check:

```python
def find_shared_modulus():
    def gcd(a,b):
        while b != 0:
            a, b = b, a % b
        return a

    moduli = [int(x,0) for x in open('mods.txt','r').read().rstrip().split('\n')]
    n = len(moduli)
    for i in range(n-1):
        for j in range(i+1,n):
            g = gcd(moduli[i], moduli[j])
            if g != 1:
                print('Shared factor between %d.pem and %d.pem' % (i+1,j+1))
                print('%#x' % g)
                print("Modulus %d:" % (i+1))
                print("%#x" % moduli[i])
                print("Modulus %d:" % (j+1))
                print("%#x" % moduli[j])

find_shared_modulus()
```

If this finds any pairs of keys that share the same factor (*p* or *q*), then you can easily obtain the other factor and create two private keys. One of them should help you retrieve the flag, although you might find the code in [rsanne](../rsanne) useful if some form of padding was used.
