pcap-me
=======

Link: https://backdoor.sdslabs.co/challenges/PCAP-me \
Tags: [n00b19CTF] [misc]

Description:
------------

Analyse a pcap file to obtain a flag.

Solution:
---------

The pcap file is not massively long, but it does contain a lot of possibly extraneous stuff like DNS queries. If you're using Wireshark, you can type `http` into the display filter text box to filter out everything except the HTTP application layer traffic (which is presumably where you would be most likely to find a flag.)

Now you only have only eleven page requests and eleven responses to look at. It shouldn't be hard to figure things out from here.
