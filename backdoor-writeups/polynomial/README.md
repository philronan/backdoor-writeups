polynomial
==========

Link: https://backdoor.sdslabs.co/challenges/polynomial \
Tags: [n00b19CTF] [misc]

Description:
------------

Get a flag by solving a mathematical challenge at an online server.

Launch the online service and you get the following prompt:

> *Let's Play a game. If you are able to solve my challenge, I will give you the flag.I will generate a random polynomial with positive integer coefficients p(x). And give you values of the polynomial at any two values of x you choose.Then I will ask you for the value of the polynomial at a point of my choice. Are you ready!* \
> *Enter your first try:*

Suppose you enter `0`. It might then print back something like this:

> *The value of f(0) is 6291698139246816152880050911721462023672624450457746546458603597472596022595235100832509335469944110782312540503277568*
> *Give me your next try:*

Enter another number, like `1`, perhaps, and you get another huge number back. It will then ask you to to calculate the value of `f(x)`, where `x` is some other value. Provide the right answer, and you get a flag.

Solution:
---------

The fact that the challenge uses *positive integer* coefficients is the key. Suppose, for example, I have the following polynomial:

> *p*(*x*) = *a*<sub>0</sub> + *a*<sub>1</sub>*x* + *a*<sub>2</sub>*x*<sup>2</sup> + ... + *a*<sub>*n*</sub>*x*<sup>*n*</sup>

If I told you that the value of *p*(1000) was 54026059041031, do you think you could take an educated guess at what the coefficient values are? Or how about if I told you the value of *p*(1000000) was 54000026000059000041000031?

I'll say nothing more, except that the values returned by the server look a lot prettier if you convert them from decimal to some other base.
