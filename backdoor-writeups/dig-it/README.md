dig-it
======

Link: https://backdoor.sdslabs.co/challenges/DIG-IT \
Tags: [n00b18CTF] [reversing]

Description:
------------

Extract a flag from a 64-bit ELF executable file.

Solution:
---------

It's often possible to use `strings` to extract hidden text from an executable file, but in this case it doesn't reveal any flags.

So open the file in your favourite disassembler and take a look. (I'm using Hopper Disassembler.)

This series of instructions at the top of the `main()` function looks interesting:

```
0000000000400cb9         mov        dword [rbp+var_90], 0x73
0000000000400cc3         mov        dword [rbp+var_8C], 0x74
0000000000400ccd         mov        dword [rbp+var_88], 0x72
0000000000400cd7         mov        dword [rbp+var_84], 0x31
0000000000400ce1         mov        dword [rbp+var_80], 0x6e
0000000000400ce8         mov        dword [rbp+var_7C], 0x67
0000000000400cef         mov        dword [rbp+var_78], 0x73
0000000000400cf6         mov        dword [rbp+var_74], 0x5f
0000000000400cfd         mov        dword [rbp+var_70], 0x34
0000000000400d04         mov        dword [rbp+var_6C], 0x72
0000000000400d0b         mov        dword [rbp+var_68], 0x33
0000000000400d12         mov        dword [rbp+var_64], 0x5f
0000000000400d19         mov        dword [rbp+var_60], 0x6e
0000000000400d20         mov        dword [rbp+var_5C], 0x30
0000000000400d27         mov        dword [rbp+var_58], 0x74
0000000000400d2e         mov        dword [rbp+var_54], 0x5f
0000000000400d35         mov        dword [rbp+var_50], 0x34
0000000000400d3c         mov        dword [rbp+var_4C], 0x6c
0000000000400d43         mov        dword [rbp+var_48], 0x77
0000000000400d4a         mov        dword [rbp+var_44], 0x34
0000000000400d51         mov        dword [rbp+var_40], 0x79
0000000000400d58         mov        dword [rbp+var_3C], 0x73
0000000000400d5f         mov        dword [rbp+var_38], 0x5f
0000000000400d66         mov        dword [rbp+var_34], 0x68
0000000000400d6d         mov        dword [rbp+var_30], 0x65
0000000000400d74         mov        dword [rbp+var_2C], 0x6c
0000000000400d7b         mov        dword [rbp+var_28], 0x70
0000000000400d82         mov        dword [rbp+var_24], 0x66
0000000000400d89         mov        dword [rbp+var_20], 0x75
0000000000400d90         mov        dword [rbp+var_1C], 0x6c
```

What do you suppose those byte values represent?
