wheres-the-f4cking-password
===========================

Link: https://backdoor.sdslabs.co/challenges/Wheres-the-f4cking-password \
Tags: none

Description:
------------

A flag has been stored in a zip file. Can you retrieve it?

Solution:
---------

The zip file is, of course, encrypted. However, we can still get some information out of it using the `zipinfo` command line utility:

```
$ zipinfo file.zip
Archive:  file.zip
Zip file size: 917 bytes, number of entries: 5
-rw-rw-r--  3.0 unx        5 TX stor 19-Jan-02 18:40 part1.txt
-rw-rw-r--  3.0 unx        5 TX stor 19-Jan-02 18:40 part2.txt
-rw-rw-r--  3.0 unx        5 TX stor 19-Jan-02 18:40 part3.txt
-rw-rw-r--  3.0 unx        5 TX stor 19-Jan-02 18:41 part4.txt
-rw-rw-r--  3.0 unx        5 TX stor 19-Jan-02 18:41 part5.txt
5 files, 25 bytes uncompressed, 25 bytes compressed:  0.0%
```

There are five files in this archive, each consisting of five bytes. If you turn on verbose listing in `zipinfo`, it will give you the CRC32 checksum of each file:

```
$ zipinfo -v file.zip | grep CRC
  32-bit CRC value (hex):                         f1792cdc
  32-bit CRC value (hex):                         9badb643
  32-bit CRC value (hex):                         33743a30
  32-bit CRC value (hex):                         a707d325
  32-bit CRC value (hex):                         1655e253
```

So, it's clear what has to be done. Write a program to check the CRC32 checksums of all possible 5-byte strings consisting of printable ASCII characters. If they match any of the above values, print them out. Then reassemble the flag from the parts you found. Have fun with that :-)
