bin-easy
========

Link: https://backdoor.sdslabs.co/challenges/BIN-EASY \
Tags: [n00b16CTF] [reversing]

Description:
------------

Extract a flag from a 32-bit ELF executable file.

Solution:
---------

This is trivial to solve. You don't need to run the program; just use the `strings` command line utility to extract the ASCII text from this file, and look for something that resembles a sha256 hash:

```
strings bin-easy | egrep '^[0-9a-f]{64}$'
```

If you open this file up in a disassembler, you'll even see that the label `flag` points directly at this string.
