find-the-baby
=============

Link: https://backdoor.sdslabs.co/challenges/FIND-THE-BABY \
Tags: [n00b18CTF] [forensics]

Description:
------------

Another mystery file. Apparently we need to find the name of a city that has been hidden somewhere.

Solution:
---------

First of all, let's see what sort of file we're dealing with here:

```
$ file usb.dd
usb.dd: ISO 9660 CD-ROM filesystem data 'CDROM'
```

Some sort of disk image, apparently. MacOS reports that this can be opened the [The Unarchiver](https://theunarchiver.com). That results in a folder called `usb` full of various images and some rather interesting reading material. (Thanks, Backdoor!)

I think it would be unfair of me to tell you exactly what to look for in here, but I'll just <!-- 😏 --> comment that once you find the hidden <!-- GPS -->  data, you'll probably need to go online to discover the name of the city.
