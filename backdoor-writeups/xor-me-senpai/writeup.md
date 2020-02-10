xor-me-senpai
=============

Link: https://backdoor.sdslabs.co/challenges/XOR-me-senpai \
Tags: [misc] [crypto] [n00b20ctf]

Description:
------------

You are provided with a PNG file that won't open in any graphics application. A quick look at the contents of this file shows why:

    $ xxd secretzz.png | head
    00000000: e760 7e25 3037 743a 3062 3d30 2778 7430  .`~%07t:0b=0'xt0
    00000010: 3d3d 6ad2 3062 3e97 6636 3062 3d0c 44ca  ==j.0b>.f60b=.D.
    00000020: f962 3d1e 4e4a 643a 496f 0f47 1012 4f52  .b=.NJd:Io.G..OR
    00000030: 0859 5c07 1d49 1740 5542 5845 0756 3062  .Y\..I.@UBXE.V0b
    00000040: 45e7 c3ab 59f4 6184 1fb5 cf01 2863 6c20  E...Y.a.....(cl
    00000050: a8f5 becc 72dd f0a9 ca4a ff75 4611 ad51  ....r....J.uF..Q
    00000060: 3f16 e5c8 5f68 884b 3f53 e11c ee44 d7dd  ?..._h.K?S...D..
    00000070: c24c b34f c1c5 6471 40d5 ea28 12f8 9d17  .L.O..dq@..(....
    00000080: c5b6 50cd 23c3 af5d a292 af97 c79d d2f2  ..P.#..]........
    00000090: dfc7 1f9f c6ba f18b 011e 41e2 770f e215  ..........A.w...

This is all wrong; all PNG files should start with the following signature:

    00000000: 8950 4e47 0d0a 1a0a                      .PNG....        

Solution
--------

The title of this challenge strongly suggests that the file has been encrypted by XOR-ing it with a secret key. If so, we can easily discover the first 8 bytes of this key by XOR-ing this file signature with the first 8 bytes of `secretzz.png`:

    >>> hex(0x89504e470d0a1a0a ^ 0xe7607e253037743a)
    '0x6e3030623d3d6e30L'
    >>> '6e3030623d3d6e30'.decode('hex')
    'n00b==n0'

It looks like the encryption was done using the repeating key `noob==`. Applying this key to the entire file is simple enough. And sure enough, this results in a valid PNG image containing the flag. (I'll leave the coding as an exercise for the reader.)
