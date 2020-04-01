stego
=====

Link: https://backdoor.sdslabs.co/challenges/STEGO \
Tags: [scythe16] [misc]

Description:
------------

Not many clues with this one. You just get a file called `que` and you have to extract a flag from it.

Solution:
---------

If you look at a hex dump of this file, you should see something familiar at the end:

```
000006c0: 7b82 06c5 dcba a47d 8b3a 28f6 d34d 92ba  {......}.:(..M..
000006d0: 1aab 247a 4eb8 291d 2522 46a3 b6a4 47c6  ..$zN.).%"F...G.
000006e0: 1446 db6f c998 ed9c 7854 4144 49d9 0600  .F.o....xTADI...
000006f0: 00f4 0909 c23f 3f3f 9f9f 9f5f 5f5f dfdf  .....???...___..
00000700: dfbf bfbf 7f7f 7f1f 1f1f ffff ff00 0000  ................
00000710: 4554 4c50 1b00 0000 295e b518 0000 0003  ETLP....)^......
00000720: 0496 0000 0026 0200 0052 4448 490d 0000  .....&...RDHI...
00000730: 000a 1a0a 0d47 4e50 89                   .....GNP.
```

Can you see it yet? Yes, that's right. This is the header of a PNG file, but in reverse order. In fact the whole file is a PNG. You just need to reverse the byte order.

```
$ python <<<'s=open("que","rb").read()[::-1]; open("image.png","wb").write(s)'
```

Open up the resulting image file, and there's your flag. I'm not sure this even qualifies as "steganography", but whatever.

Just one small caveat. The last term in the flag image clearly starts with a zero, but to get the flag accepted, you'll need to replace this with a capital O.
