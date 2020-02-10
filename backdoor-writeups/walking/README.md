walking
=======

Link: https://backdoor.sdslabs.co/challenges/Walking \
Tags: [forensics] [n00b20ctf]

Description:
------------

The challenge consists of an image file (bing.jpg) and the message "Sometimes an image contains more than it looks."

Solution
--------

A quick inspection in a hex editor showed that a zip archive has been tacked onto the end of this file. This is what `zipinfo` made of it:

    $ zipinfo bing.jpg
    Archive:  bing.jpg
    Zip file size: 25300 bytes, number of entries: 2
    warning [bing.jpg]:  24907 extra bytes at beginning or within zipfile
      (attempting to process anyway)
    drwxr-xr-x  2.0 unx        0 bx stor 20-Jan-07 13:38 Found/
    -rw-r--r--  2.0 unx       33 bX defN 20-Jan-07 13:38 Found/flag.txt
    2 files, 33 bytes uncompressed, 35 bytes compressed:  -6.1%

It's not even encrypted. Just unzip the file and you're done:

    $ unzip bing.jpg
    Archive:  bing.jpg
    warning [bing.jpg]:  24907 extra bytes at beginning or within zipfile
      (attempting to process anyway)
       creating: Found/
      inflating: Found/flag.txt          
