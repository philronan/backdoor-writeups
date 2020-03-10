logo
====

Link: https://backdoor.sdslabs.co/challenges/LOGO \
Tags: [scythe15] [steganography]

Description:
------------

Find the hidden flag in a PNG file.

Solution:
---------

I'm not sure "hidden" is really the right word here. There is clearly something going on in the bottom few lines of this image, starting about two thirds of the way along the 458th line. It's a simple binary code; all you need to do is figure out which pixels correspond to `1` and which to `0`. It's really not that hard to figure it out.
