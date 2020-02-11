php-pro
=========

Link: https://backdoor.sdslabs.co/challenges/php-pro \
Tags: [web] [n00b20ctf]

Description:
------------

You're given a link to a web page coded in PHP, presumably with some sort of vulnerability.

    $ curl --include 'http://hack.bckdr.in:17582'
    HTTP/1.1 200 OK
    Host: hack.bckdr.in:17582
    Date: Tue, 11 Feb 2020 01:18:53 +0000
    Connection: close
    X-Powered-By: PHP/7.1.25
    Content-type: text/html; charset=UTF-8



    <html>
    <head>
    <title>Komi San can't compare</title>
    <body>
    <img src = "https://static.zerochan.net/M%E2%80%99Aider.Sounan.Girl.full.1625366.jpg">
    <h1>No Flag for you - Komi San</h1></body>
    </head>
    </html>

Solution
--------

A common flaw in PHP CTF challenges (and, I guess, out in the wild) is the use of the following syntax to check a user's login credentials:

    if (strcmp($_GET['password'], 'letmein') == 0) {
        $logged_in = true;
    }

The `strcmp()` function returns zero if the two string parameters are the same. But if one of the parameters passed to it is an array, it raises a warning and returns NULL. Unfortunately, NULL and zero are essentially the same as far as the above comparison statement is concerned.

It's easy to pass an array to `$_GET` via the query string; just put a pair of square brackets `[]` after the token name (or `%5B%5D` when urlencoded). For example:

    http://hack.bckdr.in:17582/?password%5B%5D=0

But instead of `password`, you'll need to find the correct token name. It's not that difficult, really.
