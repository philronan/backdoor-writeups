noobsource
==========

Link: https://backdoor.sdslabs.co/challenges/Noobsource \
Tags: [n00b19CTF] [misc] [web]

Description:
------------

Extract a flag from the source code of a web page

Solution:
---------

The page tries to prevent users from viewing the source code by using Javascript to disable keypress and right-click events, and by redirecting the visitor to [about:blank](about:blank) after two seconds.

How do I know this? I looked at the source code, of course. And it's not hard to find the flag in there. I'll leave you to figure out the details.
