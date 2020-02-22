skilzz
======

Link: https://backdoor.sdslabs.co/challenges/Skilzz \
Tags: [pwn] [frontdoorctf]

Description:
------------

The challenge here is to extract a flag from a bash server with a restricted set of available commands.

Solution:
---------

When you connect to the server via netcat, the commands you type in are treated as input to a bash console, except that most commands are unavailable.

So for example `pwd` will tell you that you're in the `/challenge` directory, but `ls` will result in an error message (`ls: not found`). However, there are other ways of getting a file listing. For example:

```
for f in * ; do echo $f ; done
```

The list of files includes one called `flag.txt`. This is promising. But unfortunately, `cat flag.txt` doesn't work either. Is there perhaps another way of printing the contents of a file without using `cat`? You might find this link useful: https://stackoverflow.com/q/7427262/1679849
