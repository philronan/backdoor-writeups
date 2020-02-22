crashes
=======

Link: https://backdoor.sdslabs.co/challenges/crashes \
Tags: [web] [frontdoorctf]

Description:
------------

You need to find a way of extracting the flag from this PHP script:

```PHP
<?php

include 'flag.php';

$a = (string)$_GET['a'];
$b = (string)$_GET['b'];

if(empty($a) || empty($b)){
    highlight_file('index.php');
    die();
}

if ($a == $b){
    die("Nope...");
}
else{
    if(md5($a) == md5($b)){
        die($FLAG);
    }
    else{
        die("Naadaa...");
    }
}

?>
```

Solution:
---------

It looks like we need to request this page with a query string containing two different parameters `a` and `b` that have the same MD5 hash. In other words, we have to find an MD5 collision. Now that MD5 is thoroughly broken, there are plenty of examples to choose from. [The shortest examples appear to be 64-byte binary strings.](https://crypto.stackexchange.com/q/15873/11718)

However, PHP has a special quirk that allows you to get the flag with query strings that are much shorter. One of the links provided as reference describes the following [quirky behaviour of PHP](https://www.owasp.org/images/6/6b/PHPMagicTricks-TypeJuggling.pdf#page=9):

> **PHP Comparisons: Loose**
>
> It gets weirder... If PHP decides that both operands look like numbers,
> even if they are actually strings, it will convert them both and perform
> a numeric comparison:
>
> ▪ `TRUE: "0e12345" == "0e54321"` \
> ▪ `TRUE: "0e12345" <= "1"` \
> ▪ `TRUE: "0e12345" == "0"` \
> ▪ `TRUE: "0xF" == "15"`
>
> Less impact, but still important.

Any two strings that consist of the characters `0e` followed by a string of decimal digits will be considered to be equal by PHP, because it converts them to floating-point numbers before performing the comparison. For example, `0e3` and `0e6` will be converted to `0.0E+03` and `0.0E+06`, which are equal because they both correspond to floating-point zero.

Unfortunately, a lot of MD5 hashes also consist of `0e` followed by a string of 30 decimal digits. If you look around on the web, you'll find some examples easily enough. (Two well-known ones appear in the flag itself.)

Or you could even generate your own strings. Assuming the hex digits of MD5 hashes are uniformly distributed, the probability of obtaining a hash of this sort is equal to 1 in 340,282,366 (=256 / (10/16)^30). On a desktop PC, it should be possible to find several examples in less than an hour. While writing this up, I found four examples with a program I left running in the background.

**Note:** As stated in most references, a *strict* comparison (using `===` instead of `==`) would avoid this problem, but if you want to write secure code, you should always use a constant-time string comparison method when checking hashes. And obviously you should never use MD5 at all.
