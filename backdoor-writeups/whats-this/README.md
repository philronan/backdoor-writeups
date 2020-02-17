whats-this
==========

Link: https://backdoor.sdslabs.co/challenges/whats-this \
Tags: [forensics] [frontdoorctf]

Description:
------------

Extract the flag from a zip file.

Solution
--------

Use `zipinfo` to peek inside the file:

```
$ zipinfo UwU.zip
Archive:  UwU.zip
Zip file size: 31745 bytes, number of entries: 11
-rw----     2.0 fat     1341 bl defN 19-Oct-13 02:41 word/numbering.xml
-rw----     2.0 fat     1770 bl defN 19-Oct-13 02:41 word/settings.xml
-rw----     2.0 fat     1370 bl defN 19-Oct-13 02:41 word/fontTable.xml
-rw----     2.0 fat     4575 bl defN 19-Oct-13 02:41 word/styles.xml
-rw----     2.0 fat     5987 bl defN 19-Oct-13 02:41 word/document.xml
-rw----     2.0 fat     1076 bl defN 19-Oct-13 02:41 word/_rels/document.xml.rels
-rw----     2.0 fat      298 bl defN 19-Oct-13 02:41 _rels/.rels
-rw----     2.0 fat       70 bl defN 19-Oct-13 02:41 word/media/image2.png
-rw----     2.0 fat     7643 bl defN 19-Oct-13 02:41 word/theme/theme1.xml
-rw----     2.0 fat    29749 bl defN 19-Oct-13 02:41 word/media/image1.png
-rw----     2.0 fat     1119 bl defN 19-Oct-13 02:41 [Content_Types].xml
11 files, 54998 bytes uncompressed, 30299 bytes compressed:  44.9%
```

I recognised this straight away. If you don't know what this file structure corresponds to, [here's a major hint](https://en.wikipedia.org/wiki/Office_Open_XML_file_formats).
