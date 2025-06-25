link-preview
============

Link: https://backdoor.sdslabs.co/challenges/polynomial \
Tags: [n00b19CTF] [web]

Description:
------------

Someone has written a web caching service that stores a client-side copy of web content in a cookie. Can you use this to access a local file called `flag.txt`?

Solution:
---------

We don't know the absolute file path of `flag.txt` on the server, but in any case, typing `file:///flag.txt` into the URL entry field doesn't work. The form will only accept URLs that start with `http://` or `https://`. So let's try caching a small file and see what happens. Try this for example:

```
http://backdoor.sdslabs.co/robots.txt
```

There's a hint that the solution to this challenge involves using PHP's `serialize()` function. And if you open up developer tools in your browser, you'll see a serialized PHP array stored as a cookie called `cachedObject`. If you unserialize it, it will look something like this:

```
__PHP_Incomplete_Class Object
(
    [__PHP_Incomplete_Class_Name] => LinkPreview
    [link:LinkPreview:private] => http://backdoor.sdslabs.co/robots.txt
    [data:LinkPreview:private] => User-agent: BLEXBot
Disallow: /

)
```

Don't worry about the `Incomplete_Class` warnings. When you click the **View Cached Data!** button, this is what will be used to show you the cached content. Now try changing the URL to `file:///flag.txt` (making sure that the serialized data remains valid). No errors, but you're still seeing the same cached data, right? Well, what if the `LinkPreview` item was missing? Can you figure out what to do now?
