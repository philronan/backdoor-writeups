weekly-2-challenge-1
=======================

Link: https://backdoor.sdslabs.co/challenges/weekly-2-1 \
Tags: [crypto] [weekly2]

Description:
------------

This is an RSA challenge in two parts.


Solution:
---------

When you connect to the remote server, you're presented with this puzzle:

```
n =  14594526805528734291285794770307986141123407358463049896...etc...(617 digits)
c =  62322358110060777554275724547213261461428710934287446553...etc...(575 digits)
e < 100
Enter the decoded message to proceed further
```

To find out the plaintext message `m`, notice the small value of `e` and the fact that `c` is several orders of magnitude smaller than `n`. This strongly suggests that `m**e` is smaller than `n`. If so, we should be able to factorise `c` to discover both `m` and `e`. This turns out to be correct.

For the second part of the challenge, you have some different numbers to work with:

```
n1 =  1575845143687565130424234569057766827583175527439186365...etc...(309 digits)
n2 =  1575845143687565130424234569057766827583175527439186365...etc...(309 digits)
c =  15152005328189473215163957549195497305108010632780089994...etc...(309 digits)
What is your decoded message?
```

According to the Python source code provided as part of the challenge, `n1` is the product of two primes `p` and `q`, and `n2` is equal to `(p+4) * (q+4)`.

By simple algebra, `p+q = (n2-n1-16)/4`. Since we now have expressions for `p+q` and `p*q`, we can find `p` and `q` by solving a quadratic equation. I'll leave you to figure out the details.

All you have to do then is plug the correct values for `p`, `q`, `c` and `e` into the [RSA code](textbook_rsa.py) to undo the double encryption used in `run.py` and get a plaintext message that will allow you to retrieve the key.

```Python
cc = rsa_decrypt(p+4,q+4,c,e,False)
rsa_decrypt(p,q,cc,e)
```

```
