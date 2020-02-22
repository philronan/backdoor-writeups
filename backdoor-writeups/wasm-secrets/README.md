wasm-secrets
============

Link: https://backdoor.sdslabs.co/challenges/wasm-secrets \
Tags: [n00b19CTF] [reversing]

Description:
------------

Extract a flag from a web assembly module.

Solution:
---------

You're given a web assembly text (.wat) file to look at, but it isn't much use. Just follow the link to the online server. View the HTML source code, and this will tell you where the compiled web assembly file (.wasm) is being loaded from. Download this to your computer, then use `strings` to extract the text portions of the code, including the flag.

You'll need to wrap the flag with `CTF{...}` to get it accepted.
