lottery
=======

Link: https://backdoor.sdslabs.co/challenges/lottery \
Tags: [pwn] [frontdoorctf]

Description:
------------

Given the source code of an online lottery program, find a way of winning the lottery with fewer than the expected number of attempts.

Solution
--------

Winning the lottery requires the player to correctly guess six numbers from 1 to 42. These are the lines from `lottery.c` that generate the prize-winning numbers:

```C
for(i=0; i<6; i++){
    lottery[i] = (lottery[i] % 42) + 1;             // 1 ~ 42
}
```

The probability of getting all six numbers correct is equal to 1 in 5,245,786 (not 1 in 8,145,060 as stated in the lottery program itself; that would be for a lottery with 6 numbers from 1 to 45). Either way, connecting to the remote server this many times would take quite a while.

But there's a short cut. Here's the code that checks the numbers (actually ASCII values from `\x01` to `\x2a`) supplied by the user:

```C
// calculate lottery score
int match = 0, j = 0;
for(i=0; i<6; i++){
    for(j=0; j<6; j++){
        if(lottery[i] == submit[j]){
            match++;
        }
    }
}

// win!
if(match == 6){
        system("/bin/cat flag.txt");
}
else{
        printf("bad luck...\n");
}
```

Can you see the problem with this code? If you choose your numbers carefully, the chance of winning drops to 1 in 7.
