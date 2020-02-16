simple
======

Link: https://backdoor.sdslabs.co/challenges/Simple \
Tags: [pwn] [frontdoorctf]

Description:
------------

You're given a 64-bit ELF binary, its C source code, and a URL where the program can be accessed at a remote server. You're also give some pretty clear instructions to the effect that you need to use a buffer overflow exploit to obtain the flag.

Solution
--------

The C source code is very short:

```C
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

void flag(){
	char flag[64];
	printf("Oh! No you found the flag\n");
	FILE *f = fopen("flag.txt","r");
	fgets(flag,64,f);
	printf(flag);
	fflush(stdout);
}

void vuln(){
	char buf[49];
	gets(buf);
	printf("No flag for you");
	fflush(stdout);
}

int main(int argc, char **argv){
	printf("Make a wish");
	vuln();
	fflush(stdout);
}
```

Clearly to obtain the key, we need to overwrite the return address of the `vuln()` function so that control passes to the `flag()` function instead of returning to `main()`.

Instead of starting up a 64-bit Linux VM, I opened the executable file in the free demo version of Hopper Disassembler on my iMac. This showed that the `vuln()` function is located at `0x0000000000400723`, and the `flag()` function is located at `0x00000000004006c6`.

So, remembering to convert the address to little-endian byte order, we need to send the bytes `"\xc6\x06\x40\x00\x00\x00\x00\x00"` via netcat to the application on the remote server. This has to be preceded by enough additional bytes to shift this value to the exact location of the return address in the call stack. This can either be done by picking apart the disassembled code, or by writing a bash script to try sucessive values starting from 49 (the defined length of the input buffer).
