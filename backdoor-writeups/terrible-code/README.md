terrible-code
=============

Link: https://backdoor.sdslabs.co/challenges/TERRIBLE-CODE \
Tags: [n00b18CTF] [web] [reversing]

Description:
------------

Unravel a client-side password verification script to obtain a flag.

Solution:
---------

Check the HTML source and it's pretty clear what's going on. You need to enter a password that will pass the `verify()` function. To make your task slightly harder, it uses an array of helper functions with obscure names. For example, the calculation `a + b` is written as `b['gTePc'](a, b)`. If you undo this level of obfuscation, you'll end up with something like this:

```javascript
function xverify(pwd) {
  if((pwd.length == 13) &&
     (pwd[6] == pwd[10]) &&
     (pwd[10] == pwd[11]) &&
     (pwd[7] == pwd[12]) &&
     (pwd[4] == pwd[8]) &&
     (pwd[0] == pwd[9]) &&
     ((pwd.charCodeAt(10) - 40) == 8) &&
     ((pwd.charCodeAt(1) - pwd.charCodeAt(11) - 1) * 0x32145486 == 0) &&
     (((pwd.charCodeAt(3) - pwd.charCodeAt(1) - 1) * 0x2468413) == 0x2468413) &&
     ((pwd.charCodeAt(7) / 14) == 7) && ((pwd.charCodeAt(7) % 14) == 0) &&
     ((pwd.charCodeAt(2) - pwd.charCodeAt(12)) == 1) &&
     ((pwd.charCodeAt(0) % 11) == 0) && ((pwd.charCodeAt(0) % 10) == 0) &&
     (((pwd.charCodeAt(5) / 2) + 0x1302) == 0x1337) &&
     ((pwd.charCodeAt(4) >> 3) == 11) && ((pwd.charCodeAt(4) % 8) == 7)
  ){
    alert('Congratz, here is your flag :~ CTF{' + pwd +'}')
  } else{
    alert('just_kidding_lol_lol_lol_lol_lol_lol_lol_lol_lol_lol_lol_lol_lol_lol_lol_lol_lol_lol_lol');
  }
}
```

It should be pretty obvious how to arrive at the correct password from this.
