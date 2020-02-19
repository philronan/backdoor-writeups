easy-flipp
==========

Link: https://backdoor.sdslabs.co/challenges/Easy-Flipp \
Tags: [n00b19CTF] [crypto]

Description:
------------

Capture a flag by executing a CBC bit-flipping attack.

Solution:
---------

The link provided as reference tells you [pretty much all you need to know](https://masterpessimistaa.wordpress.com/2017/05/03/cbc-bit-flipping-attack/). It's obvious which bit you need to flip in order to change the message from `admin=0` into `admin=1`. And that's all there is to it.
