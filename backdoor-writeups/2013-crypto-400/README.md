2013-crypto-400
===============

Link: https://backdoor.sdslabs.co/challenges/2013-CRYPTO-400 \
Tags: [crypto]

Description:
------------

Given the source code of an encryption algorithm, decode the following ciphertext:

```
168 232 100 162 135 179 112 100 173 206 106 123 106 195 179 157 123 173
```

Solution:
---------

The encryption code is quite short. What it does can be summarized as follows:

1. Convert the plaintext into an array of byte values (e.g., `'Hello, world'` &rarr; `[72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100]`)
2. Choose a random value between 10 and the maximum value in this array (e.g., **K = 87**)
3. Multiply this value by 101 (**K \*= 101** &rarr; **K = 8787**)
4. Transform each byte **X** of the plaintext: **C = ((K + X) \* 0.5 + √(K \* X)) % 255**
5. Output this array of transformed values as the ciphertext: **[124, 31, 66, 66, 81, 192, 94, 120, 81, 96, 66, 25]**

This algorithm might look rather difficult to reverse, but there are two things working in our favour:

1. The key space is tiny. If the input plaintext consists of printable ASCII, the key value must be an integer in the range 10–126. That's only 117 possible values we need to test.
2. The encryption is monoalphabetic. In other words, the same character in the plaintext will always be encrypted as the same value in the ciphertext. (Notice the three occurrences of **66** in the above example.)

So all we need to do is test every possible key value by encrypting every printable ASCII character to find out what its corresponding value in the ciphertext would be. It turns out that there is only one key value for which each number in the ciphertext corresponds to a printable ASCII character (in the range from 32 to 126). I don't need to program this for you, do I?
