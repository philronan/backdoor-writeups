heads-or-tails
==============

Link: https://backdoor.sdslabs.co/challenges/Heads-or-Tails \
Tags: none

Description:
------------

Hack into a "heads-or-tails" guessing game to retrieve a flag.

Solution:
---------

Download the binary file and open it in your favourite disassembler. You should find a function called `secret_function()` at 0x0804851b that isn't called from anywhere in the program. It must be time to put on your stack-smashing hat.

Fortunately for us, there's a call to `gets()` inside the `input_name()` function at 0x08048639. So all we have to do is enter a name that runs past the end of the input buffer (16 bytes?) plus a bit further so we can plant the location of `secret_function()` as the return address...

...Aaaand it doesn't work! On closer examination, it appears that `secret_function()` will only give up the flag if you've scored at least 100 points in the game. No time for that nonsense. Just jump straight past the score checking code and get that flag. I'll leave you to sort out the details.
