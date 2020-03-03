2013-bin-100
============

Link: https://backdoor.sdslabs.co/challenges/2013-BIN-100 \
Tags: [reversing]

Description:
------------

Extract a flag from another 64-bit (or 32-bit) ELF file. We even have the source code this time!

Solution:
---------

The source code is a bit misleading. It swaps `argc` and `argv` in the arguments to `main()`, and uses some rather unhelpful variable names.

But without examining it in great detail, we can at least see that the program expects three or more command line arguments. It will select one of these at random, and then calculate a hash string using a customised MD5 hash function. If the hash value doesn't match, it prints out a message that appears to refer to hash collisions.

Perhaps someone has found a hash value that collides with itself after 3 million iterations? Maybe that hash value in the `check()` function has something to do with it? To be honest, I don't entirely understant what's going on here. All I know is that if you launch the program with three command line arguments all equal to this hash string, then it will give you the flag.
