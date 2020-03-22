find-me
=======

Link: https://backdoor.sdslabs.co/challenges/FIND-ME \
Tags: [n00b17CTF] [misc]

Description:
------------

The challenge says "Find the flag in `flag.txt`". But you're not given a text file. Instead you have a gzipped TAR file called `find_me.tar.gz`.

Solution:
---------

Well the first step is obviously to unpack this compressed archive:

```
$ tar -xvf find_me.tar.gz
```

Well just look at that. Screenfuls of nested directories. The top level directory is called `100`, so I guess there are 99 others beneath it. You could just pick through that and look for the filename. Or you could take a hint from the challenge name and use the `find` utility to look for files in this haystack:

```
$ find 100 -type f
```

There it is. And you can use the same command to help you print out the file:

```
$ cat `find 100 -type f`
```
