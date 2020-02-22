no-calm
=======

Link: https://backdoor.sdslabs.co/challenges/NO-CALM \
Tags: [backdoorctf17] [reversing]

Description:
------------

Extract a flag from a 64-bit ELF binary.

Solution:
---------

Open up the `challenge` executable in a disassembler and take a look at the `main()` function.

It should be fairly clear what's going on. First it checks the value of `argc`. If it doesn't equal 31, then it exits with the following message:

```
Usage ./challenge <each byte of flag separated by spaces>
```

Since `argc` is one more than the number of command line arguments, that means we're looking for a flag that is 30 characters in length.

Next, there's a bit of code to convert these arguments into a single string (0x40081f–0x40085c), and then the real fun begins:

```
    movzx      eax, byte [rbp+var_30]
    movsx      edx, al
    movzx      eax, byte [rbp+var_2F]
    movsx      eax, al
    add        edx, eax
    movzx      eax, byte [rbp+var_2E]
    movsx      eax, al
    sub        edx, eax
    mov        eax, edx
    cmp        eax, 0x51
    jne        loc_400d66

    ; etc...etc...etc...
```

This is the code that checks your input. The location `rbp+var_30` corresponds to the first byte of the input string (`$rbp - 0x30`), `rbp+var_2F` corresponds to the second byte (`$rbp - 0x2f`) and so on. You could, if you like, just work through this manually to figure out the flag, but that would be rather tedious.

Instead, let's convert this assembly into something we can run. I'm going to use Python. A text editor that supports regular expressions will make this task relatively painless. Bear in mind that your disassembler may produce assembly code that looks a bit different to what I have here, but however you approach it, there are only a few assembly instructions you need to convert. I'll assume that the flag consists of a list of ASCII values (integers) called `s`, and I'll use variables `a` and `d` to represent the `$eax` and `$edx` registers. Use a text editor to make the following changes:

1. Replace `movzx      eax, byte [rbp+var_••]` with `a = flag[48-0x••]`
2. Replace `movsx      edx, al` with `d = a`
3. Replace `movsx      eax, al` with `a = a` (Byte/word twiddling: You could just ignore it)
4. Replace `add        edx, eax` with `d += a`
5. Replace `add        eax, edx` with `a += d`
6. Replace `sub        edx, eax` with `d -= a`
7. Replace `mov        eax, edx` with `a = d`
8. Replace `cmp        eax, 0x••` with `if a != 0x••:`
9. Replace `jne        loc_••••••` with `return err` (indented) followed by `err += 1` (not indented)

Then wrap your code inside a bit of Python to initialize the `err` counter and so on. You should end up with something that looks a bit like this:

```python
def check_flag(flag):
    if len(flag) != 30:
        return "Wrong length (should be 30)"
    #
    err = 0
    #
    a = flag[48-0x30]
    d = a
    a = flag[48-0x2F]
    a = a
    d += a
    a = flag[48-0x2E]
    a = a
    d -= a
    a = d
    if a != 0x51:
        return err
    err += 1
    #
    a = flag[48-0x30]
    d = a
    a = flag[48-0x2F]
    a = a
    d -= a
    a = flag[48-0x2E]
    a = a
    a += d
    if a != 0x35:
        return err
    err += 1
    #
    # # # # # # # # # # # # # # # # # # # # # # #
    #
    #    SKIPPING 300+ LINES OF CODE. I'M NOT
    #      JUST GIVING THIS AWAY, YOU KNOW!
    #
    # # # # # # # # # # # # # # # # # # # # # # #
    #
    a = flag[48-0x14]
    d = a
    a = flag[48-0x15]
    a = a
    d -= a
    a = flag[48-0x13]
    a = a
    a += d
    if a != 0x7d:
        return err
    err += 1
    return err
```

What you should now have is a function that will test a flag (provided as a list of integer byte values) and tell you how many correct characters there are before the first error. If it returns a value of 30, then you have the correct flag.

Now all you need is a function that tests a few characters at a time (3 seems to be sufficient) and builds the flag incrementally:

```python
def crack_no_calm():
    flag = [ord('?')] * 30
    for i in range(28):
        best_depth = i
        best_flag = flag[::]
        ith_char_found = False
        for ch1 in range(32,127):
            flag[i] = ch1
            for ch2 in range(32,127):
                flag[i+1] = ch2
                for ch3 in range(32,127):
                    flag[i+2] = ch3
                    depth = check_flag(flag)
                    if depth > best_depth:
                        best_depth = depth
                        best_flag = flag[::]
        flag = best_flag[::]
        print(''.join(chr(ch) for ch in flag))
```

It's kinda slow, but it works.
