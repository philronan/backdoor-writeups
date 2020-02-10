teenage-rsa
===========

Link: https://backdoor.sdslabs.co/challenges/Teenage-RSA \
Tags: [crypto] [n00b20ctf]

Description:
------------

It's another RSA problem:

    e = 10313126904907659154044035721366030299232309115...[309 digits in total]
    n = 10968701687227089548500226697032871271028689426...[309 digits in total]
    c = 71590607059186777818957166319828787840306992214...[308 digits in total]

The value for `e` is much larger than expected. Perhaps this cipher uses a large `e` and a small `d`?

Solution
--------

Let's test a few small values of `d` and see what happens:

    x = pow(c,e,n)
    d = 2
    while True:
        if pow(x,d,n) == c:
            print "d = %d" % d
            break
        d += 1

Sure enough, the value of `d` is 65537. As a result, the message can be decrypted very easily:

    print hex(pow(c,65537,n))[2:].rstrip('L').decode('hex')
