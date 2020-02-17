conversion
==========

Link: https://backdoor.sdslabs.co/challenges/conversion \
Tags: [pwn] [frontdoorctf]

Description:
------------

It sounds like we need to exploit a vulnerability related to casting, or [type conversion](https://en.wikipedia.org/wiki/Type_conversion), as it's sometimes called. You're given a 64-bit ELF executable file, and the location of an online instance of this program.

Solution
--------

Connect to the online server, and you get this prompt:

```
Welcome to The Conversion Ring
Enter a number less than 1000
```

If you enter any number from 0 to 1000, it just prints the message `Think Harder` and exits. Any larger number results in a different message: `Told ya, the value should be less than 1000`.

So can you enter a number less than 1000 that isn't in the range 0–1000? The answer is glaringly obvious, really...
