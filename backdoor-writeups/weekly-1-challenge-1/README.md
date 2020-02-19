weekly-1-challenge-1
====================

Link: https://backdoor.sdslabs.co/challenges/weekly-1-1 \
Tags: [pwn] [weekly1]

Description:
------------

You're given the address of an online service that asks for your name and prints it back to you, and a copy of the 64-bit ELF executable file used by this service.


Solution:
---------

This is a really basic buffer overflow challenge. First open the file `chall1` in a disassembler (I'm using the free version of Hopper Disassembler). Notice (a) the call to `gets()` at 0x00000000004006bd, and (b) the unreachable function `win()` at 0x00000000004006db. It looks like `gets()` is being passed a 32-byte buffer. How far past the end of that do you have to go to reach the return address of this function? And what bytes do you need to overwrite this return address with? This should all be fairly obvious, but if not, you should perhaps go and read [Smashing The Stack For Fun And Profit](http://www-inst.eecs.berkeley.edu/~cs161/fa08/papers/stack_smashing.pdf).
