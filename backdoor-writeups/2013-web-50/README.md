2013-web-50
===========

Link: https://backdoor.sdslabs.co/challenges/2013-WEB-50 \
Tags: [web]

Description:
------------

Capture a flag by gaining admin privileges on a web site.

Solution:
---------

When you follow the link, all you see is the following message:

```
You are not admin
```

There's nothing to interact with here, so let's take a look at the HTTP headers instead:

```
curl --include http://hack.bckdr.in:10003
HTTP/1.1 200 OK
Host: hack.bckdr.in:10003
Date: Tue, 03 Mar 2020 18:57:10 +0000
Connection: close
X-Powered-By: PHP/7.1.25
Set-Cookie: username=john
Content-type: text/html; charset=UTF-8

You are not admin
```

Notice the `Set-Cookie` header. The server has decided that my username is `john`. What if I were to request the same page with a `Cookie` header containing a different value for `username`. Like `admin`, perhaps?
