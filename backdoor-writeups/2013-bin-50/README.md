2013-bin-50
===========

Link: https://backdoor.sdslabs.co/challenges/2013-BIN-50 \
Tags: [reversing]

Description:
------------

Extract a flag from a 64-bit (or 32-bit) ELF file.

Solution:
---------

Running `strings` is always a good idea when looking for hidden clues inside an executable file. This was no exception:

```
l$ L
t$(L
|$0H
Password is Advicemallard
qie////3213/wqeqwe/qwqweqsxcf/d/////
Password is Butter
Password is Hoobastank
Password is Darth
Password is Jedimaster
Password is Masternamer
Password is Morpheus
Password is Neutron
Password is Coyote
Password is Tweety
Nothing to see here.
Please provide the password
;*3$"
GCC: (Ubuntu/Linaro 4.6.3-1ubuntu5) 4.6.3
.symtab
.strtab
.shstrtab
```

Try running the program, and when it asks for a password, use one of these.
