weekly-2-challenge-4
====================

Link: https://backdoor.sdslabs.co/challenges/weekly-2-4 \
Tags: [web] [weekly2]

Description:
------------

You get a [link to a web page](http://hack.bckdr.in:15108/). All it says is:

```
Welcome to the weekly challenge. A n00b is using django to hide his secrets.
```


Solution:
---------

Maybe we can guess the URL of the flag file? Try http://hack.bckdr.in:15108/flag.txt

> **Page not found (404)**
>
> **Request Method:** GET \
> **Request URL:** http://hack.bckdr.in:15108/flag.txt \
> Using the URLconf defined in `weekly404.urls`, Django tried these URL patterns, in this order:
>
> 1. `^$`
> 2. `^flag/`
>
> The current path, `flag.txt`, didn't match any of these.
> You're seeing this error because you have `DEBUG = True` in your Django settings file. Change that to `False`, and Django will display a standard 404 page.


Well that's interesting. Django is telling us that there is no file called `flag.txt`, but there is a directory called `flag`. If we request a page called `flag/nosuchfile`, then we can get a list of all the files in the `flag` directory too. It turns out there are quite a lot of them. How are you going to check them all?
