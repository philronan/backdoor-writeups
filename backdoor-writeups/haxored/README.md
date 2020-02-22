haxored
=======

Link: https://backdoor.sdslabs.co/challenges/haXORed \
Tags: [crypto] [frontdoorctf]

Description:
------------

Extract the flag from a file `flag.enc`, which contains the following hex string:

```
232924223e27373031761a23753726761a74361a241a262d71372838
```

Solution:
---------

The challenge page hints in a very unsubtle way that the flag has been encrypted by XORing each byte with the same value. So just try every possible value, and if the resulting text contains the word 'flag', print it out. Easy peasy.
