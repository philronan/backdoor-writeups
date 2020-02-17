what-the-f0x
============

Link: https://backdoor.sdslabs.co/challenges/what-the-f0x \
Tags: [steganography] [n00b20ctf]

Description:
------------

Extract a flag from a long text file containing nothing but the characters `[`, `]`, `(`, `)` `+` and `!`.

Solution:
---------

The Wikipedia link is a massive hint. This is indeed code written in an esoteric language. If you're having trouble figuring out which particular language, you could perhaps look at the entries for the [shortest "Hello, World!" program](https://codegolf.stackexchange.com/questions/55422/hello-world) at codegolf.stackexchange.com.

Once you know what language it is, it should be easy to figure out where you can execute this code. All it does is print out the flag.
