shounen-rsa
===========

Link: https://backdoor.sdslabs.co/challenges/ReallySimplyAlgorithm \
Tags: [crypto] [frontdoorctf]

Description:
------------

Another twist on the textbook RSA theme.

Solution:
---------

This is very similar to [really-simple-algorithm](../really-simple-algorithm), except that in this case we are given the two prime factors of `n`. Well, almost. Their values are XORed with random 8-bit values, so all we need to do is try every possible value of `x1` (from 0 to 255). One of these will be a factor of `n`. Using this value, we can obtain `p` and `q`, allowing us to calculate `d` and decrypt the ciphertext.
